"""Abstract models for the CoherentPluggableSubscription. NO is_base=True."""

from enum import StrEnum

from orchestrator.domain.base import SubscriptionModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.abstracts.product_blocks.coherent_pluggable import (
    AbstractCoherentPluggableBlockActive,
    AbstractCoherentPluggableBlockInactive,
    AbstractCoherentPluggableBlockProvisioning,
)


class VendorPartNumber(StrEnum):
    """Enumerate supported optical device vendor and part numbers."""

    CISCO_QDD_400G_ZRP_S = "CISCO QDD-400G-ZRP-S"
    CISCO_DP04QSDD_HK9 = "CISCO DP04QSDD-HK9"


class AbstractCoherentPluggableSubscriptionInactive(SubscriptionModel):
    """Abstract base model for an optical node subscription in the INACTIVE state."""

    vendor_part_number: VendorPartNumber
    transceiver: AbstractCoherentPluggableBlockInactive


class AbstractCoherentPluggableSubscriptionProvisioning(
    SubscriptionModel, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """Abstract base model for an optical node subscription in the Provisioning state."""

    vendor_part_number: VendorPartNumber
    transceiver: AbstractCoherentPluggableBlockProvisioning


class AbstractCoherentPluggableSubscriptionActive(SubscriptionModel, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    """Abstract base model for an optical node subscription in the ACTIVE state."""

    vendor_part_number: VendorPartNumber
    transceiver: AbstractCoherentPluggableBlockActive
