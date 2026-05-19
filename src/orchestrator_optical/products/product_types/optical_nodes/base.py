"""Module that defines the Product Types for optical nodes."""

from abc import ABC
from enum import StrEnum

from orchestrator.domain.base import SubscriptionModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_nodes.base import (
    AbstractOpticalNodeBlockInactive,
)

# --- Enums ---


class VendorPlatform(StrEnum):
    """Enumerate supported optical device vendor and models."""

    NOKIA_GROOVE_G30 = "Nokia Groove G30"
    NOKIA_FLEXILS = "Nokia FlexILS"
    NOKIA_GX_G42 = "Nokia GX G42"


# --- Abstract Base Models ---
# These are not assigned 'is_base=True' so they remain internal templates.


class AbstractOpticalNodeSubscriptionInactive(
    ABC,
    SubscriptionModel,
    lifecycle=[SubscriptionLifecycle.INITIAL],
):
    """Abstract base model for an optical node subscription in the INACTIVE state."""

    vendor_platform: VendorPlatform
    node: AbstractOpticalNodeBlockInactive
