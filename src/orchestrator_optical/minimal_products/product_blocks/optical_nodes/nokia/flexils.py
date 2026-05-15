"""Nokia FlexILS product blocks."""

from typing import Annotated, Literal

from annotated_types import Len
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_nodes.base import (
    AbstractOpticalNodeBlock,
    AbstractOpticalNodeBlockInactive,
    AbstractOpticalNodeBlockProvisioning,
    DeviceFunction,
)
from orchestrator_optical.utils.custom_types.ip_address import IPAddress

IpAddressesList = Annotated[
    list[IPAddress], Len(min_length=1, max_length=10), "List of the management IP addresses of the device."
]

# --- Nokia FlexILS Product Blocks ---
# These are abstract base models for Nokia FlexILS product blocks. They are not assigned a `product_block_name`.
# Every organization must subclass and register its own concrete blocks based on these templates, with a specific
# `product_block_name` and any additional fields needed.


class AbstractNokiaFlexIlsBlockInactive(AbstractOpticalNodeBlockInactive, lifecycle=[SubscriptionLifecycle.INITIAL]):
    """Abstract base class for Nokia FlexILS product blocks in the Inactive state."""

    device_function: Literal[DeviceFunction.ROADM, DeviceFunction.AMPLIFIER]
    gmpls_id: IPAddress | None = None


class AbstractNokiaFlexIlsBlockProvisioning(
    AbstractNokiaFlexIlsBlockInactive,
    AbstractOpticalNodeBlockProvisioning,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base class for Nokia FlexILS product blocks in the Provisioning state."""

    gmpls_id: IPAddress


class AbstractNokiaFlexIlsBlock(
    AbstractNokiaFlexIlsBlockProvisioning, AbstractOpticalNodeBlock, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for Nokia FlexILS product blocks in the Active state."""
