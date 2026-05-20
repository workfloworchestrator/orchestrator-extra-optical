"""Abstract classes for OpticalDigitalService product blocks."""

from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle
from pydantic import Field

from orchestrator_optical.abstracts.product_blocks.coherent_pluggable import (
    AbstractCoherentPluggableBlock,
    AbstractCoherentPluggableBlockInactive,
    AbstractCoherentPluggableBlockProvisioning,
)
from orchestrator_optical.abstracts.product_blocks.optical_port import (
    AbstractTransponderClientPortBlock,
    AbstractTransponderClientPortBlockInactive,
    AbstractTransponderClientPortBlockProvisioning,
)
from orchestrator_optical.abstracts.product_blocks.transport_channel import (
    AbstractOpticalTransportChannelBlock,
    AbstractOpticalTransportChannelBlockInactive,
    AbstractOpticalTransportChannelBlockProvisioning,
)

ClientPortsList = Annotated[list[SI], Len(min_length=2, max_length=2)]

Clients = Annotated[AbstractTransponderClientPortBlock | AbstractCoherentPluggableBlock, Field(discriminator="role")]
ClientsProvisioning = Annotated[
    AbstractTransponderClientPortBlockProvisioning | AbstractCoherentPluggableBlockProvisioning,
    Field(discriminator="role"),
]
ClientsInactive = Annotated[
    AbstractTransponderClientPortBlockInactive | AbstractCoherentPluggableBlockInactive, Field(discriminator="role")
]

TransportChannelsList = Annotated[
    list[SI], Len(min_length=1, max_length=2)
]  # if 2 then reverse multiplexing: 2 transport channels for one client service


class AbstractOpticalDigitalServiceBlockInactive(ProductBlockModel):
    """Abstract base class for inactive Optical Digital Service product blocks."""

    service_name: str | None = None
    client_ports: ClientPortsList[AbstractTransponderClientPortBlockInactive]
    transport_channels: TransportChannelsList[AbstractOpticalTransportChannelBlockInactive]


class AbstractOpticalDigitalServiceBlockProvisioning(
    AbstractOpticalDigitalServiceBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """Abstract base class for provisioning Optical Digital Service product blocks."""

    service_name: str
    client_ports: ClientPortsList[AbstractTransponderClientPortBlockProvisioning]
    transport_channels: TransportChannelsList[AbstractOpticalTransportChannelBlockProvisioning]


class AbstractOpticalDigitalServiceBlock(
    AbstractOpticalDigitalServiceBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active Optical Digital Service product blocks."""

    client_ports: ClientPortsList[Clients]
    transport_channels: TransportChannelsList[AbstractOpticalTransportChannelBlock]
