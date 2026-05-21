from abc import ABC, abstractmethod
from enum import StrEnum
from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.domain.context_cache import get_from_cache
from pydantic import computed_field

from orchestrator_optical.protocols.location import LocationProtocol
from orchestrator_optical.utils.custom_types.fqdn import Fqdn
from orchestrator_optical.utils.custom_types.ip_address import IPAddress

IpAddressesList = Annotated[
    list[IPAddress], Len(min_length=1, max_length=10), "List of the management IP addresses of the device."
]


class NodeRole(StrEnum):
    """Device type based on its functionalities. Since chasses are modular, the type can change during device's life."""

    ROADM = "ROADM"
    AMPLIFIER = "Amplifier"
    TRANSPONDER = "Transponder"
    TRANSPONDER_XOADM = "Transponder and xOADM"


class AbstractOpticalNodeBlockInactive(ProductBlockModel, ABC):
    """Base Product Block for Optical Nodes."""

    sw_version: str | None = None
    fqdn: Fqdn | None = None
    role: NodeRole | None = None
    management_ips: IpAddressesList | None = None

    @property
    @abstractmethod
    def location(self) -> LocationProtocol:
        """The location where the node is housed MUST be implemented as a **field** in the concrete implementation."""
        ...

    @computed_field  # because it comes from the subscription fixed_inputs
    @property
    def vendor_platform(self) -> str:
        """The vendor and platform of the node, e.g. 'Nokia FlexILS'."""
        # Tier 1: Query the domain model context cache (Fastest, 0 DB queries)
        cached_sub = get_from_cache(self.subscription_id)
        if cached_sub:
            return cached_sub.vendor_platform

        # Tier 2: Scan pre-loaded SQLAlchemy relationship (Prevents N+1 queries)
        if self.subscription and self.subscription.product:
            for fi in self.subscription.product.fixed_inputs:
                if fi.name == "vendor_platform":
                    return fi.value

        msg = f"Fixed input 'vendor_platform' not found for subscription {self.owner_subscription_id}"
        raise ValueError(msg)


class AbstractOpticalNodeBlockProvisioning(AbstractOpticalNodeBlockInactive, ABC):
    """Base Product Block for Optical Nodes in provisioning state."""

    fqdn: Fqdn
    role: NodeRole
    management_ips: IpAddressesList


class AbstractOpticalNodeBlock(AbstractOpticalNodeBlockProvisioning, ABC):
    """Base Product Block for Optical Nodes in operational state."""

    sw_version: str
