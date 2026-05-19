"""Nokia FlexILS product blocks."""

from abc import ABC
from typing import Annotated, Literal

from annotated_types import Len
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_nodes.base import (
    AbcOpticalNodeBlock,
    AbcOpticalNodeBlockInactive,
    AbcOpticalNodeBlockProvisioning,
    NodeRole,
)
from orchestrator_optical.products.product_types.optical_nodes.base import VendorPlatform
from orchestrator_optical.utils.custom_types.ip_address import IPAddress

IpAddressesList = Annotated[
    list[IPAddress], Len(min_length=1, max_length=10), "List of the management IP addresses of the device."
]


class AbcNokiaFlexIlsBlockInactive(ABC, AbcOpticalNodeBlockInactive, lifecycle=[SubscriptionLifecycle.INITIAL]):
    """Abstract base class for Nokia FlexILS product blocks in the Inactive state."""

    role: Literal[NodeRole.ROADM, NodeRole.AMPLIFIER]
    gmpls_id: IPAddress | None = None
    vendor_platform: VendorPlatform = VendorPlatform.NOKIA_FLEXILS


class AbcNokiaFlexIlsBlockProvisioning(
    ABC,
    AbcNokiaFlexIlsBlockInactive,
    AbcOpticalNodeBlockProvisioning,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base class for Nokia FlexILS product blocks in the Provisioning state."""

    gmpls_id: IPAddress


class AbcNokiaFlexIlsBlock(
    ABC, AbcNokiaFlexIlsBlockProvisioning, AbcOpticalNodeBlock, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for Nokia FlexILS product blocks in the Active state."""
