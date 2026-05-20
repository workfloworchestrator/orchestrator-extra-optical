"""Module for Optical Pipe product blocks (Fiber Patch, Fiber Span, and Leased Spectrum)."""

from typing import Annotated

from pydantic import Field

from orchestrator_optical.abstracts.product_blocks.optical_pipe import (
    AbstractFiberPatchBlock,
    AbstractFiberPatchBlockInactive,
    AbstractFiberPatchBlockProvisioning,
    AbstractFiberSpanBlock,
    AbstractFiberSpanBlockInactive,
    AbstractFiberSpanBlockProvisioning,
    AbstractLeasedSpectrumBlock,
    AbstractLeasedSpectrumBlockInactive,
    AbstractLeasedSpectrumBlockProvisioning,
    ListOfPorts,
)
from orchestrator_optical.products.product_blocks.coherent_pluggable import (
    CoherentPluggable,
    CoherentPluggableInactive,
    CoherentPluggableProvisioning,
)
from orchestrator_optical.products.product_blocks.optical_port import (
    OlsAddDropPort,
    OlsAddDropPortInactive,
    OlsAddDropPortProvisioning,
    OlsLinePort,
    OlsLinePortInactive,
    OlsLinePortProvisioning,
    TransponderClientPort,
    TransponderClientPortInactive,
    TransponderClientPortProvisioning,
    TransponderLinePort,
    TransponderLinePortInactive,
    TransponderLinePortProvisioning,
)

# --- Concrete Port Unions for Patch Pipes ---

PatchPortBlocksInactive = Annotated[
    TransponderClientPortInactive | TransponderLinePortInactive | OlsAddDropPortInactive | CoherentPluggableInactive,
    Field(discriminator="role"),
]

PatchPortBlocksProvisioning = Annotated[
    TransponderClientPortProvisioning
    | TransponderLinePortProvisioning
    | OlsAddDropPortProvisioning
    | CoherentPluggableProvisioning,
    Field(discriminator="role"),
]

PatchPortBlocks = Annotated[
    TransponderClientPort | TransponderLinePort | OlsAddDropPort | CoherentPluggable,
    Field(discriminator="role"),
]


# --- Concrete Port Unions for Span Pipes ---

SpanPortBlocksInactive = OlsLinePortInactive
SpanPortBlocksProvisioning = OlsLinePortProvisioning
SpanPortBlocks = OlsLinePort


# --- Concrete Port Unions for Leased Spectrum Pipes ---

LeasedSpectrumPortBlocksInactive = Annotated[
    TransponderLinePortInactive | OlsAddDropPortInactive | OlsLinePortInactive | CoherentPluggableInactive,
    Field(discriminator="role"),
]

LeasedSpectrumPortBlocksProvisioning = Annotated[
    TransponderLinePortProvisioning
    | OlsAddDropPortProvisioning
    | OlsLinePortProvisioning
    | CoherentPluggableProvisioning,
    Field(discriminator="role"),
]

LeasedSpectrumPortBlocks = Annotated[
    TransponderLinePort | OlsAddDropPort | OlsLinePort | CoherentPluggable,
    Field(discriminator="role"),
]


# ============================================================================
# --- Fiber Patch Product Blocks ---
# ============================================================================


class FiberPatchInactive(AbstractFiberPatchBlockInactive, product_block_name="FiberPatch"):
    """Inactive state of a Fiber Patch product block."""

    terminations: ListOfPorts[PatchPortBlocksInactive]


class FiberPatchProvisioning(FiberPatchInactive, AbstractFiberPatchBlockProvisioning):
    """Provisioning state of a Fiber Patch product block."""

    terminations: ListOfPorts[PatchPortBlocksProvisioning]


class FiberPatch(FiberPatchProvisioning, AbstractFiberPatchBlock):
    """Active state of a Fiber Patch product block."""

    terminations: ListOfPorts[PatchPortBlocks]


# ============================================================================
# --- Fiber Span Product Blocks ---
# ============================================================================


class FiberSpanInactive(AbstractFiberSpanBlockInactive, product_block_name="FiberSpan"):
    """Inactive state of a Fiber Span product block."""

    terminations: ListOfPorts[SpanPortBlocksInactive]


class FiberSpanProvisioning(FiberSpanInactive, AbstractFiberSpanBlockProvisioning):
    """Provisioning state of a Fiber Span product block."""

    terminations: ListOfPorts[SpanPortBlocksProvisioning]


class FiberSpan(FiberSpanProvisioning, AbstractFiberSpanBlock):
    """Active state of a Fiber Span product block."""

    terminations: ListOfPorts[SpanPortBlocks]


# ============================================================================
# --- Leased Spectrum Product Blocks ---
# ============================================================================


class LeasedSpectrumInactive(AbstractLeasedSpectrumBlockInactive, product_block_name="LeasedSpectrum"):
    """Inactive state of a Leased Spectrum product block."""

    terminations: ListOfPorts[LeasedSpectrumPortBlocksInactive]


class LeasedSpectrumProvisioning(LeasedSpectrumInactive, AbstractLeasedSpectrumBlockProvisioning):
    """Provisioning state of a Leased Spectrum product block."""

    terminations: ListOfPorts[LeasedSpectrumPortBlocksProvisioning]


class LeasedSpectrum(LeasedSpectrumProvisioning, AbstractLeasedSpectrumBlock):
    """Active state of a Leased Spectrum product block."""

    terminations: ListOfPorts[LeasedSpectrumPortBlocks]
