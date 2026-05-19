"""Module that defines the Minimal Product Type for coherent pluggables."""

from enum import StrEnum

from orchestrator.domain.base import SubscriptionModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.minimal_products.product_blocks.coherent_pluggable import (
    CoherentPluggableBlock,
    CoherentPluggableBlockInactive,
    CoherentPluggableBlockProvisioning,
)

# --- Types & Enums---


class Vendor(StrEnum):
    """Enumerate supported optical device vendors."""

    NOKIA = "Nokia"
    CISCO = "Cisco"
    JUNIPER = "Juniper"


class PartNumber(StrEnum):
    """Enumerate supported optical device models."""

    CISCO_QDD_400G_ZR_S = "CISCO QDD-400G-ZR-S"
    CISCO_QDD_400G_ZRP_S = "CISCO QDD-400G-ZRP-S"
    CISCO_DP04QSDD_HK9 = "CISCO DP04QSDD-HK9"


# --- Minimal Product Types ---


class CoherentPluggableSubscriptionInactive(SubscriptionModel, is_base=True):
    """Base model for a coherent pluggable subscription in the INACTIVE state."""

    vendor: Vendor
    part_number: PartNumber
    pluggable: CoherentPluggableBlockInactive


class CoherentPluggableSubscriptionProvisioning(
    CoherentPluggableSubscriptionInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """Base model for a coherent pluggable subscription in the PROVISIONING state."""

    pluggable: CoherentPluggableBlockProvisioning


class CoherentPluggableSubscriptionActive(
    CoherentPluggableSubscriptionProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Base model for a coherent pluggable subscription in the ACTIVE state."""

    pluggable: CoherentPluggableBlock
