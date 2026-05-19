"""Optical spectrum service product type subscription models."""

from abc import ABC

from orchestrator.domain.base import SubscriptionModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_spectrum import (
    AbstractOpticalSpectrumBlock,
    AbstractOpticalSpectrumBlockInactive,
    AbstractOpticalSpectrumBlockProvisioning,
)


class AbstractOpticalSpectrumServiceInactive(
    ABC,
    SubscriptionModel,
    lifecycle=[SubscriptionLifecycle.INITIAL],
):
    """Abstract base model for an optical spectrum service subscription in the INACTIVE state."""

    spectrum: AbstractOpticalSpectrumBlockInactive


class AbstractOpticalSpectrumServiceProvisioning(
    ABC,
    AbstractOpticalSpectrumServiceInactive,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base model for an optical spectrum service subscription in the PROVISIONING state."""

    spectrum: AbstractOpticalSpectrumBlockProvisioning


class AbstractOpticalSpectrumService(
    AbstractOpticalSpectrumServiceProvisioning,
    lifecycle=[SubscriptionLifecycle.ACTIVE],
):
    """Abstract base model for an optical spectrum service subscription in the ACTIVE state."""

    spectrum: AbstractOpticalSpectrumBlock
