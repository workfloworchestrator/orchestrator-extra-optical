from enum import StrEnum
from typing import Literal

from orchestrator.domain.base import SubscriptionModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.abstracts.product_blocks.optical_node import (
    AbstractOpticalNodeBlock,
    AbstractOpticalNodeBlockInactive,
    AbstractOpticalNodeBlockProvisioning,
    NodeRole,
)
from orchestrator_optical.products.product_blocks.deleteme_location import ReplaceMeLocation
from orchestrator_optical.utils.custom_types.ip_address import IPAddress


class OpticalNodeInactive(AbstractOpticalNodeBlockInactive, product_block_name="OpticalNode"):
    location: ReplaceMeLocation | None = None


class OpticalNodeProvisioning(OpticalNodeInactive, AbstractOpticalNodeBlockProvisioning):
    location: ReplaceMeLocation


class OpticalNode(OpticalNodeProvisioning, AbstractOpticalNodeBlock):
    location: ReplaceMeLocation


# NokiaFlexILS model
class NokiaFlexILSNodeInactive(AbstractOpticalNodeBlockInactive, product_block_name="NokiaFlexILSNode"):
    location: ReplaceMeLocation | None = None
    role: Literal[NodeRole.ROADM, NodeRole.AMPLIFIER] | None = None
    gmpls_id: IPAddress | None = None


class NokiaFlexILSNodeProvisioning(NokiaFlexILSNodeInactive, AbstractOpticalNodeBlockProvisioning):
    location: ReplaceMeLocation
    role: Literal[NodeRole.ROADM, NodeRole.AMPLIFIER]
    gmpls_id: IPAddress


class NokiaFlexILSNode(NokiaFlexILSNodeProvisioning, AbstractOpticalNodeBlock):
    pass
