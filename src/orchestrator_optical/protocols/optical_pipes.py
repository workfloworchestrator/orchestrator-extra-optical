"""Workflow execution contracts for physical fibers and leased spectrum."""

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from orchestrator_optical.protocols.optical_ports import (
    OlsAddDropPortProtocol,
    OlsLinePortProtocol,
    TrxClientInterfaceProtocol,
    TrxLineInterfaceProtocol,
)

# Type aliases representing allowed terminations
PatchPortProtocols = TrxClientInterfaceProtocol | TrxLineInterfaceProtocol | OlsAddDropPortProtocol
SpanPortProtocols = OlsLinePortProtocol
LeasedSpectrumPortProtocols = TrxLineInterfaceProtocol | OlsAddDropPortProtocol | OlsLinePortProtocol


@runtime_checkable
class FiberProtocol(Protocol):
    """Base contract for any physical fiber link."""

    fiber_name: str


@runtime_checkable
class OpticalPatchProtocol(FiberProtocol, Protocol):
    """Protocol for a patch cord."""

    terminations: Sequence[PatchPortProtocols]  # Exactly 2


@runtime_checkable
class OpticalSpanProtocol(FiberProtocol, Protocol):
    """Protocol for a fiber span between OLS elements."""

    terminations: Sequence[SpanPortProtocols]  # Exactly 2


@runtime_checkable
class LeasedSpectrumProtocol(Protocol):
    """Protocol for a leased spectrum over third-party infrastructure."""

    leased_spectrum_name: str
    terminations: Sequence[LeasedSpectrumPortProtocols]  # Exactly 2
