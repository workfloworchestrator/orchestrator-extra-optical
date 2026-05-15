"""Workflow execution contracts for Transport Channels and Digital Services."""

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from orchestrator_optical.contracts.optical_ports import TrxClientInterfaceContract, TrxLineInterfaceContract
from orchestrator_optical.contracts.optical_spectrum import OpticalSpectrumContract


@runtime_checkable
class OpticalTransportChannelContract(Protocol):
    """Contract for an Optical Transport Channel (Layer 0)."""

    channel_name: str
    central_frequency: int
    transceiver_mode: str
    line_ports: Sequence[TrxLineInterfaceContract]  # Exactly 2
    spectrum: OpticalSpectrumContract


@runtime_checkable
class OpticalDigitalServiceContract(Protocol):
    """Contract for an Optical Digital Service (Client facing)."""

    service_name: str
    client_ports: Sequence[TrxClientInterfaceContract]  # Exactly 2
    transport_channels: Sequence[OpticalTransportChannelContract]  # 1 to 2
