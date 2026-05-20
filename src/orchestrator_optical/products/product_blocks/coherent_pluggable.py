from orchestrator_optical.abstracts.product_blocks.coherent_pluggable import (
    AbstractCoherentPluggableBlock,
    AbstractCoherentPluggableBlockInactive,
    AbstractCoherentPluggableBlockProvisioning,
)
from orchestrator_optical.products.product_blocks.deleteme_packetnode import ReplaceMePacketNode


class CoherentPluggableInactive(AbstractCoherentPluggableBlockInactive, product_block_name="CoherentPluggable"):
    host_node: ReplaceMePacketNode | None = None


class CoherentPluggableProvisionig(CoherentPluggableInactive, AbstractCoherentPluggableBlockProvisioning):
    host_node: ReplaceMePacketNode


class CoherentPluggable(CoherentPluggableProvisionig, AbstractCoherentPluggableBlock):
    host_node: ReplaceMePacketNode
