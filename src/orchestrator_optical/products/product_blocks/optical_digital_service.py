"""Module for Optical Digital Service product blocks."""

from typing import Annotated

from pydantic import Field

from orchestrator_optical.abstracts.product_blocks.optical_digital_service import (
    AbstractOpticalDigitalServiceBlock,
    AbstractOpticalDigitalServiceBlockInactive,
    AbstractOpticalDigitalServiceBlockProvisioning,
    ClientPortsList,
    TransportChannelsList,
)
from orchestrator_optical.products.product_blocks.coherent_pluggable import (
    CoherentPluggable,
    CoherentPluggableInactive,
    CoherentPluggableProvisioning,
)
from orchestrator_optical.products.product_blocks.optical_port import (
    TransponderClientPort,
    TransponderClientPortInactive,
    TransponderClientPortProvisioning,
)
from orchestrator_optical.products.product_blocks.transport_channel import (
    OpticalTransportChannel,
    OpticalTransportChannelInactive,
    OpticalTransportChannelProvisioning,
)

# --- Concrete Union Types for Client Ports ---

ClientsInactive = Annotated[TransponderClientPortInactive | CoherentPluggableInactive, Field(discriminator="role")]

ClientsProvisioning = Annotated[
    TransponderClientPortProvisioning | CoherentPluggableProvisioning, Field(discriminator="role")
]

Clients = Annotated[TransponderClientPort | CoherentPluggable, Field(discriminator="role")]


# ============================================================================
# --- Optical Digital Service Product Blocks ---
# ============================================================================


class OpticalDigitalServiceInactive(
    AbstractOpticalDigitalServiceBlockInactive, product_block_name="OpticalDigitalService"
):
    """Inactive state of an Optical Digital Service product block."""

    client_ports: ClientPortsList[TransponderClientPortInactive]
    transport_channels: TransportChannelsList[OpticalTransportChannelInactive]


class OpticalDigitalServiceProvisioning(OpticalDigitalServiceInactive, AbstractOpticalDigitalServiceBlockProvisioning):
    """Provisioning state of an Optical Digital Service product block."""

    client_ports: ClientPortsList[TransponderClientPortProvisioning]
    transport_channels: TransportChannelsList[OpticalTransportChannelProvisioning]


class OpticalDigitalService(OpticalDigitalServiceProvisioning, AbstractOpticalDigitalServiceBlock):
    """Active state of an Optical Digital Service product block."""

    client_ports: ClientPortsList[Clients]
    transport_channels: TransportChannelsList[OpticalTransportChannel]
