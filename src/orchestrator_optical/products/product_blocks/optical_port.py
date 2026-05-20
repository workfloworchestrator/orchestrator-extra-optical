from orchestrator_optical.abstracts.product_blocks.optical_port import (
    AbstractOlsAddDropPortBlock,
    AbstractOlsAddDropPortBlockInactive,
    AbstractOlsAddDropPortBlockProvisioning,
    AbstractOlsLinePortBlock,
    AbstractOlsLinePortBlockInactive,
    AbstractOlsLinePortBlockProvisioning,
    AbstractTransponderClientPortBlock,
    AbstractTransponderClientPortBlockInactive,
    AbstractTransponderClientPortBlockProvisioning,
    AbstractTransponderLinePortBlock,
    AbstractTransponderLinePortBlockInactive,
    AbstractTransponderLinePortBlockProvisioning,
)
from orchestrator_optical.products.product_blocks.optical_node import (
    OpticalNode,
    OpticalNodeInactive,
    OpticalNodeProvisioning,
)

# --- Inactive ---


class OlsAddDropPortInactive(AbstractOlsAddDropPortBlockInactive, product_block_name="OlsAddDropPort"):
    host_node: OpticalNodeInactive


class OlsLinePortInactive(AbstractOlsLinePortBlockInactive, product_block_name="OlsLinePort"):
    host_node: OpticalNodeInactive


class TransponderClientPortInactive(
    AbstractTransponderClientPortBlockInactive, product_block_name="TransponderClientPort"
):
    host_node: OpticalNodeInactive


class TransponderLinePortInactive(AbstractTransponderLinePortBlockInactive, product_block_name="TransponderLinePort"):
    host_node: OpticalNodeInactive


# --- Provisioning ---


class OlsAddDropPortProvisioning(OlsAddDropPortInactive, AbstractOlsAddDropPortBlockProvisioning):
    host_node: OpticalNodeProvisioning


class OlsLinePortProvisioning(OlsLinePortInactive, AbstractOlsLinePortBlockProvisioning):
    host_node: OpticalNodeProvisioning


class TransponderClientPortProvisioning(TransponderClientPortInactive, AbstractTransponderClientPortBlockProvisioning):
    host_node: OpticalNodeProvisioning


class TransponderLinePortProvisioning(TransponderLinePortInactive, AbstractTransponderLinePortBlockProvisioning):
    host_node: OpticalNodeProvisioning


# --- Active ---


class OlsAddDropPort(OlsAddDropPortProvisioning, AbstractOlsAddDropPortBlock):
    host_node: OpticalNode


class OlsLinePort(OlsLinePortProvisioning, AbstractOlsLinePortBlock):
    host_node: OpticalNode


class TransponderClientPort(TransponderClientPortProvisioning, AbstractTransponderClientPortBlock):
    host_node: OpticalNode


class TransponderLinePort(TransponderLinePortProvisioning, AbstractTransponderLinePortBlock):
    host_node: OpticalNode
