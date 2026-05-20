"""Abstract product blocks for optical fibers and leased spectrum."""

from enum import StrEnum
from typing import Annotated, Literal

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle
from pydantic import Field

from orchestrator_optical.abstracts.product_blocks.coherent_pluggable import (
    AbstractCoherentPluggableBlock,
    AbstractCoherentPluggableBlockInactive,
    AbstractCoherentPluggableBlockProvisioning,
)
from orchestrator_optical.abstracts.product_blocks.optical_port import (
    AbstractOlsAddDropPortBlock,
    AbstractOlsAddDropPortBlockInactive,
    AbstractOlsAddDropPortBlockProvisioning,
    AbstractOlsLinePortBlock,
    AbstractOlsLinePortBlockInactive,
    AbstractOlsLinePortBlockProvisioning,
    AbstractTransponderClientPortBlock,
    AbstractTransponderClientPortBlockInactive,
    AbstractTransponderClientPortBlockProvisioning,
    AbstractTransponderLinePortBlock,
    AbstractTransponderLinePortBlockInactive,
    AbstractTransponderLinePortBlockProvisioning,
)

ListOfPorts = Annotated[list[SI], Len(min_length=2, max_length=2), "List of the 2 ports connected by the fiber."]


class PipeRole(StrEnum):
    """missing docstring."""

    PATCH = "Fiber Patch"
    SPAN = "Fiber Span"
    LEASED_SPECTRUM = "Leased Spectrum"


PatchPortBlocks = Annotated[
    AbstractTransponderClientPortBlock
    | AbstractTransponderLinePortBlock
    | AbstractOlsAddDropPortBlock
    | AbstractCoherentPluggableBlock,
    Field(discriminator="role"),
]
PatchPortBlocksInactive = Annotated[
    AbstractTransponderClientPortBlockInactive
    | AbstractTransponderLinePortBlockInactive
    | AbstractOlsAddDropPortBlockInactive
    | AbstractCoherentPluggableBlockInactive,
    Field(discriminator="role"),
]
PatchPortBlocksProvisioning = Annotated[
    AbstractTransponderClientPortBlockProvisioning
    | AbstractTransponderLinePortBlockProvisioning
    | AbstractOlsAddDropPortBlockProvisioning
    | AbstractCoherentPluggableBlockProvisioning,
    Field(discriminator="role"),
]


SpanPortBlocks = AbstractOlsLinePortBlock
SpanPortBlocksInactive = AbstractOlsLinePortBlockInactive
SpanPortBlocksProvisioning = AbstractOlsLinePortBlockProvisioning


LeasedSpectrumPortBlocks = Annotated[
    AbstractTransponderLinePortBlock
    | AbstractOlsAddDropPortBlock
    | AbstractOlsLinePortBlock
    | AbstractCoherentPluggableBlock,
    Field(discriminator="role"),
]
LeasedSpectrumPortBlocksInactive = Annotated[
    AbstractTransponderLinePortBlockInactive
    | AbstractOlsAddDropPortBlockInactive
    | AbstractOlsLinePortBlockInactive
    | AbstractCoherentPluggableBlockInactive,
    Field(discriminator="role"),
]
LeasedSpectrumPortBlocksProvisioning = Annotated[
    AbstractTransponderLinePortBlockProvisioning
    | AbstractOlsAddDropPortBlockProvisioning
    | AbstractOlsLinePortBlockProvisioning
    | AbstractCoherentPluggableBlockProvisioning,
    Field(discriminator="role"),
]


class AbstractFiberPatchBlockInactive(ProductBlockModel):
    """missing docstring."""

    role: Literal[PipeRole.PATCH] = PipeRole.PATCH
    pipe_name: str | None = None
    terminations: ListOfPorts[PatchPortBlocksInactive]


class AbstractFiberPatchBlockProvisioning(
    AbstractFiberPatchBlockInactive, lifecycle=SubscriptionLifecycle.PROVISIONING
):
    """missing docstring."""

    terminations: ListOfPorts[PatchPortBlocksProvisioning]


class AbstractFiberPatchBlock(AbstractFiberPatchBlockProvisioning, lifecycle=SubscriptionLifecycle.ACTIVE):
    """missing docstring."""

    pipe_name: str
    terminations: ListOfPorts[PatchPortBlocks]


class AbstractFiberSpanBlockInactive(ProductBlockModel):
    """missing docstring."""

    role: Literal[PipeRole.SPAN] = PipeRole.SPAN
    pipe_name: str | None = None
    terminations: ListOfPorts[SpanPortBlocksInactive]


class AbstractFiberSpanBlockProvisioning(AbstractFiberSpanBlockInactive, lifecycle=SubscriptionLifecycle.PROVISIONING):
    """missing docstring."""

    terminations: ListOfPorts[SpanPortBlocksProvisioning]


class AbstractFiberSpanBlock(AbstractFiberSpanBlockProvisioning, lifecycle=SubscriptionLifecycle.ACTIVE):
    """missing docstring."""

    pipe_name: str
    terminations: ListOfPorts[SpanPortBlocks]


class AbstractLeasedSpectrumBlockInactive(ProductBlockModel):
    """missing docstring."""

    role: Literal[PipeRole.LEASED_SPECTRUM] = PipeRole.LEASED_SPECTRUM
    pipe_name: str | None = None
    terminations: ListOfPorts[LeasedSpectrumPortBlocksInactive]


class AbstractLeasedSpectrumBlockProvisioning(
    AbstractLeasedSpectrumBlockInactive, lifecycle=SubscriptionLifecycle.PROVISIONING
):
    """missing docstring."""

    terminations: ListOfPorts[LeasedSpectrumPortBlocksProvisioning]


class AbstractLeasedSpectrumBlock(AbstractLeasedSpectrumBlockProvisioning, lifecycle=SubscriptionLifecycle.ACTIVE):
    """missing docstring."""

    pipe_name: str
    terminations: ListOfPorts[LeasedSpectrumPortBlocks]
