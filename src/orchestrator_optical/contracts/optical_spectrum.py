"""Workflow execution contracts for Optical Spectrum and Sections."""

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from orchestrator_optical.contracts.optical_ports import OlsAddDropPortContract, OlsLinePortContract
from orchestrator_optical.utils.custom_types.frequencies import Passband


@runtime_checkable
class OpticalSpectrumSectionContract(Protocol):
    """Contract representing a segment of the spectrum path."""

    add_drop_ports: Sequence[OlsAddDropPortContract]  # Exactly 2
    express_ports: Sequence[OlsLinePortContract]  # 0 to 64


@runtime_checkable
class OpticalSpectrumContract(Protocol):
    """Contract representing the end-to-end optical spectrum."""

    spectrum_name: str
    passband: Passband
    sections: Sequence[OpticalSpectrumSectionContract]
