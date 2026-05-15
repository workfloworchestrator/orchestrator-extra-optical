"""Module that defines the Product Types for optical fibers."""

from abc import ABC

from orchestrator.domain.base import SubscriptionModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_pipes import (
    AbstractLeasedSpectrumBlockInactive,
    AbstractOpticalPatchBlockInactive,
    AbstractOpticalSpanBlockInactive,
)

# --- Abstract Base Models ---
# We use these to encapsulate the lifecycle field transitions.
# These are not assigned 'is_base=True' so they remain internal templates.


class AbstractOpticalFiberPatchInactive(ABC, SubscriptionModel, lifecycle=[SubscriptionLifecycle.INITIAL]):
    """Abstract base model for an optical fiber patch subscription in the INACTIVE state."""

    fiber: AbstractOpticalPatchBlockInactive


class AbstractOpticalFiberSpanInactive(ABC, SubscriptionModel, lifecycle=[SubscriptionLifecycle.INITIAL]):
    """Abstract base model for an optical fiber span subscription in the INACTIVE state."""

    fiber: AbstractOpticalSpanBlockInactive


class AbstractOpticalLeasedSpectrumInactive(ABC, SubscriptionModel, lifecycle=[SubscriptionLifecycle.INITIAL]):
    """Abstract base model for an optical leased spectrum subscription in the INACTIVE state."""

    spectrum: AbstractLeasedSpectrumBlockInactive
