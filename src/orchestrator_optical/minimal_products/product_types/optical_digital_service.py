"""Optical digital service product type subscription models."""

from abc import ABC
from enum import StrEnum

from orchestrator.domain.base import SubscriptionModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_digital_service import (
    AbstractOpticalDigitalServiceBlock,
    AbstractOpticalDigitalServiceBlockInactive,
    AbstractOpticalDigitalServiceBlockProvisioning,
)


class ServiceSpeedAndType(StrEnum):
    """Service speed and type enum."""

    ETHERNET_100GBPS = "100Gbps Ethernet"
    ETHERNET_400GBPS = "400Gbps Ethernet"


class AbstractOpticalDigitalServiceInactive(ABC, SubscriptionModel, is_base=True):
    """Abstract base model for an optical digital service subscription in the INACTIVE state."""

    speed_and_type: ServiceSpeedAndType
    service: AbstractOpticalDigitalServiceBlockInactive


class AbstractOpticalDigitalServiceProvisioning(
    ABC,
    AbstractOpticalDigitalServiceInactive,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base model for an optical digital service subscription in the PROVISIONING state."""

    speed_and_type: ServiceSpeedAndType
    service: AbstractOpticalDigitalServiceBlockProvisioning


class AbstractOpticalDigitalService(
    ABC,
    AbstractOpticalDigitalServiceProvisioning,
    lifecycle=[SubscriptionLifecycle.ACTIVE],
):
    """Abstract base model for an optical digital service subscription in the ACTIVE state."""

    speed_and_type: ServiceSpeedAndType
    service: AbstractOpticalDigitalServiceBlock
