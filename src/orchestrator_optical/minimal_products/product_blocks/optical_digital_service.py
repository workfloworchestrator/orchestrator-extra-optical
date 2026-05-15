"""Module for Optical Digital Service product blocks."""

from abc import ABC
from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle
from products.product_blocks.optical_ports import (
    TrxClientInterfaceBlock,
    TrxClientInterfaceBlockInactive,
    TrxClientInterfaceBlockProvisioning,
)

from orchestrator_optical.products.product_blocks.optical_transport_channel import (
    OpticalTransportChannelBlock,
    OpticalTransportChannelBlockInactive,
    OpticalTransportChannelBlockProvisioning,
)

ClientPortsList = Annotated[list[SI], Len(min_length=2, max_length=2)]

TransportChannelsList = Annotated[
    list[SI], Len(min_length=1, max_length=2)
]  # reverse multiplexing -> 2 transport channels for one client service


class AbstractOpticalDigitalServiceBlockInactive(ABC, ProductBlockModel, product_block_name="OpticalDigitalService"):
    """Abstract base class for inactive Optical Digital Service product blocks."""

    service_name: str | None = None
    client_ports: ClientPortsList[TrxClientInterfaceBlockInactive]
    transport_channels: TransportChannelsList[OpticalTransportChannelBlockInactive]


class AbstractOpticalDigitalServiceBlockProvisioning(
    ABC, AbstractOpticalDigitalServiceBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """Abstract base class for provisioning Optical Digital Service product blocks."""

    service_name: str
    client_ports: ClientPortsList[TrxClientInterfaceBlockProvisioning]
    transport_channels: TransportChannelsList[OpticalTransportChannelBlockProvisioning]


class AbstractOpticalDigitalServiceBlock(
    ABC, AbstractOpticalDigitalServiceBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active Optical Digital Service product blocks."""

    client_ports: ClientPortsList[TrxClientInterfaceBlock]
    transport_channels: TransportChannelsList[OpticalTransportChannelBlock]
