"""Abstract models for the OpticalNodeSubscription. NO is_base=True."""

from enum import StrEnum
from typing import Literal

from orchestrator.domain.base import SubscriptionModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_node import (
    NokiaFlexILSNode,
    NokiaFlexILSNodeInactive,
    NokiaFlexILSNodeProvisioning,
    OpticalNode,
    OpticalNodeInactive,
    OpticalNodeProvisioning,
)


class VendorPlatform(StrEnum):
    """Enumerate supported optical device vendor and models."""

    NOKIA_GROOVE_G30 = "Nokia Groove G30"
    NOKIA_GX_G42 = "Nokia GX G42"


class OpticalNodeSubscriptionInactive(SubscriptionModel):
    """base model for an optical node subscription in the INACTIVE state."""

    vendor_platform: VendorPlatform
    node: OpticalNodeInactive


class OpticalNodeSubscriptionProvisioning(
    OpticalNodeSubscriptionInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """base model for an optical node subscription in the Provisioning state."""

    node: OpticalNodeProvisioning


class OpticalNodeSubscriptionActive(OpticalNodeSubscriptionProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    """base model for an optical node subscription in the ACTIVE state."""

    node: OpticalNode


# Nokia FlexILS specialized subscription


class NokiaFlexILSNodeSubscriptionInactive(SubscriptionModel):
    """base model for an optical node subscription in the INACTIVE state."""

    vendor_platform: Literal["Nokia FlexILS"]
    node: NokiaFlexILSNodeInactive


class NokiaFlexILSNodeSubscriptionProvisioning(
    NokiaFlexILSNodeSubscriptionInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """base model for an optical node subscription in the Provisioning state."""

    node: NokiaFlexILSNodeProvisioning


class NokiaFlexILSNodeSubscriptionActive(
    NokiaFlexILSNodeSubscriptionProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """base model for an optical node subscription in the ACTIVE state."""

    node: NokiaFlexILSNode
