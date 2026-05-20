"""Abstract subscriptions for optical pipes. NO is_base=True."""

from enum import StrEnum
from typing import Annotated

from orchestrator.domain.base import SubscriptionModel
from orchestrator.types import SubscriptionLifecycle
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
)


class AbstractFiberPatchInactive(SubscriptionModel):
    """Abstract base model for an fiber patch subscription in the INACTIVE state."""

    pipe: AbstractFiberPatchBlockInactive


class AbstractFiberPatchProvisioning(SubscriptionModel, lifecycle=[SubscriptionLifecycle.PROVISIONING]):
    """Abstract base model for an fiber patch subscription in the Provisioning state."""

    pipe: AbstractFiberPatchBlockProvisioning


class AbstractFiberPatch(SubscriptionModel, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    """Abstract base model for an fiber patch subscription in the Active state."""

    pipe: AbstractFiberPatchBlock


class AbstractFiberSpanInactive(SubscriptionModel):
    """Abstract base model for an fiber Span subscription in the INACTIVE state."""

    pipe: AbstractFiberSpanBlockInactive


class AbstractFiberSpanProvisioning(SubscriptionModel, lifecycle=[SubscriptionLifecycle.PROVISIONING]):
    """Abstract base model for an fiber Span subscription in the Provisioning state."""

    pipe: AbstractFiberSpanBlockProvisioning


class AbstractFiberSpan(SubscriptionModel, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    """Abstract base model for an fiber Span subscription in the Active state."""

    pipe: AbstractFiberSpanBlock


class AbstractLeasedSpectrumInactive(SubscriptionModel):
    """Abstract base model for a leased spectrum subscription in the INACTIVE state."""

    pipe: AbstractLeasedSpectrumBlockInactive


class AbstractLeasedSpectrumProvisioning(AbstractLeasedSpectrumInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]):
    """Abstract base model for a leased spectrum subscription in the Provisioning state."""

    pipe: AbstractLeasedSpectrumBlockProvisioning


class AbstractLeasedSpectrum(AbstractLeasedSpectrumProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    """Abstract base model for a leased spectrum subscription in the Active state."""

    pipe: AbstractLeasedSpectrumBlock
