"""Abstract classes for OpticalSpectrumSection product blocks."""

from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle

from orchestrator_optical.abstracts.product_blocks.optical_port import (
    AbstractOlsAddDropPortBlock,
    AbstractOlsAddDropPortBlockInactive,
    AbstractOlsAddDropPortBlockProvisioning,
    AbstractOlsLinePortBlock,
    AbstractOlsLinePortBlockInactive,
    AbstractOlsLinePortBlockProvisioning,
)

AddDropPorts = Annotated[list[SI], Len(min_length=2, max_length=2), "List of add/drop ports."]

ExpressPorts = Annotated[list[SI], Len(min_length=0, max_length=64), "List of ports representing the express path."]


class AbstractOpticalSpectrumSectionBlockInactive(ProductBlockModel):
    """missing docstring."""

    add_drop_ports: AddDropPorts[AbstractOlsAddDropPortBlockInactive]
    express_ports: ExpressPorts[AbstractOlsLinePortBlockInactive]


class AbstractOpticalSpectrumSectionBlockProvisioning(
    AbstractOpticalSpectrumSectionBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """missing docstring."""

    add_drop_ports: AddDropPorts[AbstractOlsAddDropPortBlockProvisioning]
    express_ports: ExpressPorts[AbstractOlsLinePortBlockProvisioning]


class AbstractOpticalSpectrumSectionBlock(
    AbstractOpticalSpectrumSectionBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """missing docstring."""

    add_drop_ports: AddDropPorts[AbstractOlsAddDropPortBlock]
    express_ports: ExpressPorts[AbstractOlsLinePortBlock]
