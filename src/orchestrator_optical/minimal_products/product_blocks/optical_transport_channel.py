"""Module for Optical Transport Channel product blocks."""

from abc import ABC
from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle
from pydantic import computed_field

from orchestrator_optical.products.product_blocks.optical_ports import (
    AbstractTrxLineInterfaceBlock,
    AbstractTrxLineInterfaceBlockInactive,
    AbstractTrxLineInterfaceBlockProvisioning,
)
from orchestrator_optical.products.product_blocks.optical_spectrum import (
    AbstractOpticalSpectrumBlock,
    AbstractOpticalSpectrumBlockInactive,
    AbstractOpticalSpectrumBlockProvisioning,
)

LinePortList = Annotated[list[SI], Len(min_length=2, max_length=2)]


class AbstractOpticalTransportChannelBlockInactive(ABC, ProductBlockModel):
    """Abstract base class for inactive Optical Transport Channel product blocks."""

    channel_name: str | None = None
    central_frequency: int | None = None
    mode: str | None = None
    line_ports: LinePortList[AbstractTrxLineInterfaceBlockInactive]
    spectrum: AbstractOpticalSpectrumBlockInactive


class AbstractOpticalTransportChannelBlockProvisioning(
    ABC, AbstractOpticalTransportChannelBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """Abstract base class for provisioning Optical Transport Channel product blocks."""

    channel_name: str
    central_frequency: int
    mode: str
    line_ports: LinePortList[AbstractTrxLineInterfaceBlockProvisioning]
    spectrum: AbstractOpticalSpectrumBlockProvisioning

    @computed_field
    @property
    def title(self) -> str:
        """Get the title of the Optical Transport Channel product block."""
        first_code = self.line_ports[0].optical_device.location.code.lower()
        second_code = self.line_ports[1].optical_device.location.code.lower()
        return f"{self.channel_name}_{first_code}-{second_code}"


class AbstractOpticalTransportChannelBlock(
    ABC, AbstractOpticalTransportChannelBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active Optical Transport Channel product blocks."""

    channel_name: str
    central_frequency: int
    mode: str
    line_ports: LinePortList[AbstractTrxLineInterfaceBlock]
    spectrum: AbstractOpticalSpectrumBlock
