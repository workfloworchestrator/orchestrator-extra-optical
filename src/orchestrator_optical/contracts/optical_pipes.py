"""Workflow execution contracts for physical fibers and leased spectrum."""

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from orchestrator_optical.contracts.optical_ports import (
    OlsAddDropPortContract,
    OlsLinePortContract,
    TrxClientInterfaceContract,
    TrxLineInterfaceContract,
)

# Type aliases representing allowed terminations
PatchPortContracts = TrxClientInterfaceContract | TrxLineInterfaceContract | OlsAddDropPortContract
SpanPortContracts = OlsLinePortContract
LeasedSpectrumPortContracts = TrxLineInterfaceContract | OlsAddDropPortContract | OlsLinePortContract


@runtime_checkable
class FiberContract(Protocol):
    """Base contract for any physical fiber link."""

    fiber_name: str


@runtime_checkable
class OpticalPatchContract(FiberContract, Protocol):
    """Contract for a patch cord."""

    terminations: Sequence[PatchPortContracts]  # Exactly 2


@runtime_checkable
class OpticalSpanContract(FiberContract, Protocol):
    """Contract for a fiber span between OLS elements."""

    terminations: Sequence[SpanPortContracts]  # Exactly 2


@runtime_checkable
class LeasedSpectrumContract(Protocol):
    """Contract for a leased spectrum over third-party infrastructure."""

    leased_spectrum_name: str
    terminations: Sequence[LeasedSpectrumPortContracts]  # Exactly 2
