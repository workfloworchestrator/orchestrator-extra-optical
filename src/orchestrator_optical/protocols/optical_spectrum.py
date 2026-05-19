"""Workflow execution contracts for Optical Spectrum and Sections."""

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from orchestrator_optical.protocols.optical_ports import OlsAddDropPortProtocol, OlsLinePortProtocol
from orchestrator_optical.utils.custom_types.frequencies import Passband


@runtime_checkable
class OpticalSpectrumSectionProtocol(Protocol):
    """Protocol representing a segment of the spectrum path."""

    add_drop_ports: Sequence[OlsAddDropPortProtocol]  # Exactly 2
    express_ports: Sequence[OlsLinePortProtocol]  # 0 to 64


@runtime_checkable
class OpticalSpectrumProtocol(Protocol):
    """Protocol representing the end-to-end optical spectrum."""

    spectrum_name: str
    passband: Passband
    sections: Sequence[OpticalSpectrumSectionProtocol]
