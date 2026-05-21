"""Abstract classes for OpticalTransportChannel product blocks."""

from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle
from pydantic import Field, computed_field

from orchestrator_optical.abstracts.product_blocks.optical_coherent_pluggable import (
    AbstractCoherentPluggableBlock,
    AbstractCoherentPluggableBlockInactive,
    AbstractCoherentPluggableBlockProvisioning,
)
from orchestrator_optical.abstracts.product_blocks.optical_port import (
    AbstractTransponderLinePortBlock,
    AbstractTransponderLinePortBlockInactive,
    AbstractTransponderLinePortBlockProvisioning,
)
from orchestrator_optical.abstracts.product_blocks.optical_spectrum import (
    AbstractOpticalSpectrumBlock,
    AbstractOpticalSpectrumBlockInactive,
    AbstractOpticalSpectrumBlockProvisioning,
)

LinePortList = Annotated[list[SI], Len(min_length=2, max_length=2)]

TrxBlock = Annotated[AbstractCoherentPluggableBlock | AbstractTransponderLinePortBlock, Field(discriminator="role")]
TrxBlockProvisioning = Annotated[
    AbstractCoherentPluggableBlockProvisioning | AbstractTransponderLinePortBlockProvisioning,
    Field(discriminator="role"),
]
TrxBlockInactive = Annotated[
    AbstractCoherentPluggableBlockInactive | AbstractTransponderLinePortBlockInactive, Field(discriminator="role")
]


class AbstractOpticalTransportChannelBlockInactive(ProductBlockModel):
    """Abstract base class for inactive Optical Transport Channel product blocks."""

    channel_name: str | None = None
    central_frequency: int | None = None
    mode: str | None = None
    line_ports: LinePortList[TrxBlockInactive]
    spectrum: AbstractOpticalSpectrumBlockInactive


class AbstractOpticalTransportChannelBlockProvisioning(
    AbstractOpticalTransportChannelBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """Abstract base class for provisioning Optical Transport Channel product blocks."""

    channel_name: str
    central_frequency: int
    mode: str
    line_ports: LinePortList[TrxBlockProvisioning]
    spectrum: AbstractOpticalSpectrumBlockProvisioning

    @computed_field
    @property
    def title(self) -> str:  # TODO: decide if we keep this
        """Get the title of the Optical Transport Channel product block."""
        first_code = self.line_ports[0].host_node.location.fqdn_subdomain.lower()
        second_code = self.line_ports[1].host_node.location.fqdn_subdomain.lower()
        return f"{self.channel_name}_{first_code}-{second_code}"


class AbstractOpticalTransportChannelBlock(
    AbstractOpticalTransportChannelBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active Optical Transport Channel product blocks."""

    channel_name: str
    central_frequency: int
    mode: str
    line_ports: LinePortList[TrxBlock]
    spectrum: AbstractOpticalSpectrumBlock
