"""Module for Optical Spectrum Section product blocks."""

from abc import ABC
from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_ports import (
    AbstractOlsAddDropPortBlock,
    AbstractOlsAddDropPortBlockInactive,
    AbstractOlsAddDropPortBlockProvisioning,
    AbstractOlsLinePortBlock,
    AbstractOlsLinePortBlockInactive,
    AbstractOlsLinePortBlockProvisioning,
)

# --- Types ---

AddDropPorts = Annotated[list[SI], Len(min_length=2, max_length=2), "List of add/drop ports."]

ExpressPorts = Annotated[
    list[SI], Len(min_length=0, max_length=64), "List of ports representing the express path."
]

# --- Abstract Product Blocks ---
# We use these to encapsulate the lifecycle field transitions.
# These are not assigned a 'product_block_name' so they remain internal templates.


class AbstractOpticalSpectrumSectionBlockInactive(ABC, ProductBlockModel):
    """Abstract base class for inactive OpticalSpectrumSection product blocks."""

    add_drop_ports: AddDropPorts[AbstractOlsAddDropPortBlockInactive]
    express_ports: ExpressPorts[AbstractOlsLinePortBlockInactive]


class AbstractOpticalSpectrumSectionBlockProvisioning(
    ABC, AbstractOpticalSpectrumSectionBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """Abstract base class for provisioning OpticalSpectrumSection product blocks."""

    add_drop_ports: AddDropPorts[AbstractOlsAddDropPortBlockProvisioning]
    express_ports: ExpressPorts[AbstractOlsLinePortBlockProvisioning]


class AbstractOpticalSpectrumSectionBlock(
    ABC, AbstractOpticalSpectrumSectionBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active OpticalSpectrumSection product blocks."""

    add_drop_ports: AddDropPorts[AbstractOlsAddDropPortBlock]
    express_ports: ExpressPorts[AbstractOlsLinePortBlock]
