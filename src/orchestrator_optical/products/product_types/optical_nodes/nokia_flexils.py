"""Nokia FlexILS product type subscription models."""

from abc import ABC
from typing import Literal

from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_nodes.nokia.flexils import (
    AbstractNokiaFlexIlsBlock,
    AbstractNokiaFlexIlsBlockInactive,
    AbstractNokiaFlexIlsBlockProvisioning,
)
from orchestrator_optical.products.product_types.optical_nodes.base import (
    AbstractOpticalNodeSubscriptionInactive,
    VendorModel,
)


class AbstractNokiaFlexIlsSubscriptionInactive(
    ABC,
    AbstractOpticalNodeSubscriptionInactive,
    lifecycle=[SubscriptionLifecycle.INITIAL],
):
    """Subscription model for inactive Nokia FlexILS devices."""

    vendor_model: Literal[VendorModel.NOKIA_FLEXILS] = VendorModel.NOKIA_FLEXILS
    node: AbstractNokiaFlexIlsBlockInactive


class AbstractNokiaFlexIlsSubscriptionProvisioning(
    ABC,
    AbstractNokiaFlexIlsSubscriptionInactive,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Subscription model for Nokia FlexILS devices that are being provisioned."""

    node: AbstractNokiaFlexIlsBlockProvisioning


class AbstractNokiaFlexIlsSubscription(
    ABC,
    AbstractNokiaFlexIlsSubscriptionProvisioning,
    lifecycle=[SubscriptionLifecycle.ACTIVE],
):
    """Subscription model for active Nokia FlexILS devices."""

    node: AbstractNokiaFlexIlsBlock
