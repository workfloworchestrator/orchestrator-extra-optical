"""Module for Optical Transport Channel product blocks."""

from typing import Annotated

from pydantic import Field

from orchestrator_optical.abstracts.product_blocks.transport_channel import (
    AbstractOpticalTransportChannelBlock,
    AbstractOpticalTransportChannelBlockInactive,
    AbstractOpticalTransportChannelBlockProvisioning,
    LinePortList,
)
from orchestrator_optical.products.product_blocks.coherent_pluggable import (
    CoherentPluggable,
    CoherentPluggableInactive,
    CoherentPluggableProvisioning,
)
from orchestrator_optical.products.product_blocks.optical_port import (
    TransponderLinePort,
    TransponderLinePortInactive,
    TransponderLinePortProvisioning,
)
from orchestrator_optical.products.product_blocks.optical_spectrum import (
    OpticalSpectrum,
    OpticalSpectrumInactive,
    OpticalSpectrumProvisioning,
)

# --- Concrete Line Port Unions ---

TrxBlockInactive = Annotated[
    CoherentPluggableInactive | TransponderLinePortInactive,
    Field(discriminator="role"),
]

TrxBlockProvisioning = Annotated[
    CoherentPluggableProvisioning | TransponderLinePortProvisioning,
    Field(discriminator="role"),
]

TrxBlock = Annotated[
    CoherentPluggable | TransponderLinePort,
    Field(discriminator="role"),
]


# --- Inactive ---


class OpticalTransportChannelInactive(
    AbstractOpticalTransportChannelBlockInactive, product_block_name="OpticalTransportChannel"
):
    """Inactive state of an Optical Transport Channel product block."""

    line_ports: LinePortList[TrxBlockInactive]
    spectrum: OpticalSpectrumInactive


# --- Provisioning ---


class OpticalTransportChannelProvisioning(
    OpticalTransportChannelInactive, AbstractOpticalTransportChannelBlockProvisioning
):
    """Provisioning state of an Optical Transport Channel product block."""

    line_ports: LinePortList[TrxBlockProvisioning]
    spectrum: OpticalSpectrumProvisioning


# --- Active ---


class OpticalTransportChannel(OpticalTransportChannelProvisioning, AbstractOpticalTransportChannelBlock):
    """Active state of an Optical Transport Channel product block."""

    line_ports: LinePortList[TrxBlock]
    spectrum: OpticalSpectrum
