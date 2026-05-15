"""Base product blocks for Optical Nodes."""

from abc import ABC, abstractmethod
from enum import StrEnum
from typing import Annotated

from pydantic import computed_field

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.external_adapters.location import LocationContract
from orchestrator_optical.utils.custom_types.fqdn import Fqdn
from orchestrator_optical.utils.custom_types.ip_address import IPAddress
from orchestrator_optical.products.product_types.optical_nodes.base import VendorModel

IpAddressesList = Annotated[
    list[IPAddress], Len(min_length=1, max_length=10), "List of the management IP addresses of the device."
]


class DeviceFunction(StrEnum):
    """Device type based on its functionalities. Since chasses are modular, the type can change during device's life."""

    ROADM = "ROADM"
    AMPLIFIER = "Amplifier"
    TRANSPONDER = "Transponder"
    TRANSPONDER_XOADM = "Transponder and xOADM"


class AbstractOpticalNodeBlockInactive(ABC, ProductBlockModel, lifecycle=[SubscriptionLifecycle.INITIAL]):
    """Abstract base class for Optical Node product blocks in the Inactive state."""

    fqdn: Fqdn
    device_function: DeviceFunction
    management_ips: IpAddressesList | None = None
    sw_version: str | None = None

    @property
    @abstractmethod
    def location(self) -> LocationContract:
        """The location where the node is housed."""
        ...  # IMPLEMENTME

    @property
    @computed_field
    def vendor_model(self) -> VendorModel:
        """Get the vendor and model that are stored in the subscription as fixed_inputs."""
        fis = self.subscription.product.fixed_inputs
        return next((fi.value for fi in fis if fi.name == "vendor_model"), None)


class AbstractOpticalNodeBlockProvisioning(
    ABC, AbstractOpticalNodeBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """Abstract base class for Optical Node product blocks in the Provisioning state."""

    management_ips: IpAddressesList


class AbstractOpticalNodeBlock(ABC, AbstractOpticalNodeBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    """Abstract base class for Optical Node product blocks in the Active state."""

    sw_version: str
