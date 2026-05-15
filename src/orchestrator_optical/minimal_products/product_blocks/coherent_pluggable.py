"""Ready-to-use WFO Product Block models for coherent pluggables."""

from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.contracts.packet_node import PacketNodeContract
from orchestrator_optical.mixins.coherent_pluggable import (
    CoherentPluggableMixin,
    CoherentPluggableMixinInactive,
    CoherentPluggableMixinProvisioning,
)

# --- Standard Product Blocks ---


class CoherentPluggableBlockInactive(
    ProductBlockModel, CoherentPluggableMixinInactive, product_block_name="CoherentPluggable"
):
    """base model for a coherent pluggable block in the INACTIVE state.

    This block represents the basic properties of a coherent pluggable before it is fully provisioned.
    """

    host_node: "PacketNodeBlockInactive" | None


class CoherentPluggableBlockProvisioning(
    CoherentPluggableBlockInactive, CoherentPluggableMixinProvisioning, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """base model for a coherent pluggable block in the PROVISIONING state.

    This block ensures that all necessary fields are populated during the provisioning phase.
    """

    host_node: "PacketNodeBlockProvisioning"


class CoherentPluggableBlockActive(
    CoherentPluggableBlockProvisioning, CoherentPluggableMixin, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """base model for a coherent pluggable block in the ACTIVE state."""

    host_node: "PacketNodeBlock"
