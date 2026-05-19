"""Module for Optical Port product blocks."""

from abc import ABC
from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.host import (
    OpticalDeviceBlock,
    OpticalDeviceBlockInactive,
    OpticalDeviceBlockProvisioning,
)
from orchestrator_optical.utils.custom_types.frequencies import Passband

# --- Types ---

ListOfPassbands = Annotated[list[Passband], Len(min_length=0, max_length=128), "List of used passbands (MHz, MHz)."]

# --- Abstract Base Hierarchies ---
# We use these to encapsulate the lifecycle field transitions.
# These are not assigned a 'product_block_name' so they remain internal templates.


class AbstractPortInactive(ABC, ProductBlockModel):
    """Abstract base class for inactive optical ports."""

    host_node: OpticalDeviceBlockInactive | None = None
    port_name: str | None = None
    port_description: str | None = None


class AbstractPortProvisioning(ABC, AbstractPortInactive):
    """Abstract base class for provisioning optical ports."""

    host_node: OpticalDeviceBlockProvisioning
    port_name: str


class AbstractPortActive(ABC, AbstractPortProvisioning):
    """Abstract base class for active optical ports."""

    host_node: OpticalDeviceBlock
    port_description: str


class AbstractPassbandPortInactive(ABC, AbstractPortInactive):
    """Abstract base class for inactive optical ports with passbands."""

    used_passbands: ListOfPassbands | None = None


class AbstractPassbandPortProvisioning(ABC, AbstractPassbandPortInactive, AbstractPortProvisioning):
    """Abstract base class for provisioning optical ports with passbands."""

    used_passbands: ListOfPassbands


class AbstractPassbandPortActive(ABC, AbstractPassbandPortProvisioning, AbstractPortActive):
    """Abstract base class for active optical ports with passbands."""


# --- Abstract Product Blocks ---


# OpticalPort
class AbstractOpticalPortBlockInactive(ABC, AbstractPassbandPortInactive):
    """Abstract base class for inactive OpticalPort product blocks."""


class AbstractOpticalPortBlockProvisioning(
    ABC,
    AbstractOpticalPortBlockInactive,
    AbstractPassbandPortProvisioning,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base class for provisioning OpticalPort product blocks."""


class AbstractOpticalPortBlock(
    ABC, AbstractOpticalPortBlockProvisioning, AbstractPassbandPortActive, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active OpticalPort product blocks."""


# OlsAddDropPort
class AbstractOlsAddDropPortBlockInactive(ABC, AbstractPassbandPortInactive):
    """Abstract base class for inactive OlsAddDropPort product blocks."""


class AbstractOlsAddDropPortBlockProvisioning(
    ABC,
    AbstractOlsAddDropPortBlockInactive,
    AbstractPassbandPortProvisioning,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base class for provisioning OlsAddDropPort product blocks."""


class AbstractOlsAddDropPortBlock(
    ABC, AbstractOlsAddDropPortBlockProvisioning, AbstractPassbandPortActive, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active OlsAddDropPort product blocks."""


# OlsLinePort
class AbstractOlsLinePortBlockInactive(ABC, AbstractPassbandPortInactive):
    """Abstract base class for inactive OlsLinePort product blocks."""


class AbstractOlsLinePortBlockProvisioning(
    ABC,
    AbstractOlsLinePortBlockInactive,
    AbstractPassbandPortProvisioning,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base class for provisioning OlsLinePort product blocks."""


class AbstractOlsLinePortBlock(
    ABC, AbstractOlsLinePortBlockProvisioning, AbstractPassbandPortActive, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active OlsLinePort product blocks."""


# TrxLineInterface
class AbstractTrxLineInterfaceBlockInactive(ABC, AbstractPassbandPortInactive):
    """Abstract base class for inactive TrxLineInterface product blocks."""


class AbstractTrxLineInterfaceBlockProvisioning(
    ABC,
    AbstractTrxLineInterfaceBlockInactive,
    AbstractPassbandPortProvisioning,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base class for provisioning TrxLineInterface product blocks."""


class AbstractTrxLineInterfaceBlock(
    ABC, AbstractTrxLineInterfaceBlockProvisioning, AbstractPassbandPortActive, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active TrxLineInterface product blocks."""


# TrxClientInterface (Does NOT have used_passbands)
class AbstractTrxClientInterfaceBlockInactive(ABC, AbstractPortInactive):
    """Abstract base class for inactive TrxClientInterface product blocks."""


class AbstractTrxClientInterfaceBlockProvisioning(
    ABC,
    AbstractTrxClientInterfaceBlockInactive,
    AbstractPortProvisioning,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base class for provisioning TrxClientInterface product blocks."""


class AbstractTrxClientInterfaceBlock(
    ABC, AbstractTrxClientInterfaceBlockProvisioning, AbstractPortActive, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active TrxClientInterface product blocks."""
