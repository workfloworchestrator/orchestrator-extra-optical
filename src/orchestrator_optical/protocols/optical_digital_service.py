"""Workflow execution contracts for Transport Channels and Digital Services."""

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from orchestrator_optical.protocols.optical_ports import TrxClientInterfaceProtocol, TrxLineInterfaceProtocol
from orchestrator_optical.protocols.optical_spectrum import OpticalSpectrumProtocol


@runtime_checkable
class OpticalTransportChannelProtocol(Protocol):
    """Protocol for an Optical Transport Channel (Layer 0)."""

    channel_name: str
    central_frequency: int
    transceiver_mode: str
    line_ports: Sequence[TrxLineInterfaceProtocol]  # Exactly 2
    spectrum: OpticalSpectrumProtocol


@runtime_checkable
class OpticalDigitalServiceProtocol(Protocol):
    """Protocol for an Optical Digital Service (Client facing)."""

    service_name: str
    client_ports: Sequence[TrxClientInterfaceProtocol]  # Exactly 2
    transport_channels: Sequence[OpticalTransportChannelProtocol]  # 1 to 2
