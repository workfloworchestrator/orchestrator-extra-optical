from abc import ABC, abstractmethod
from enum import StrEnum
from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlock
from pydantic import Field, computed_field

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


class AbcOpticalNodeInactive(ProductBlock, ABC):
    """Base Product Block for Optical Nodes."""

    sw_version: str | None = Field(None, description="The software version of the node.")
    fqdn: Fqdn | None = Field(None, description="The Fully Qualified Domain Name of the node.")
    role: NodeRole | None = Field(
        None, description="The role of the node. Since chasses are modular, the type can change during device's life."
    )
    management_ips: IpAddressesList | None = Field(
        None,
        description="The management IP addresses of the node.",
    )

    @computed_field
    @property
    def vendor_platform(self) -> str:
        """The vendor and platform of the node, e.g. 'Nokia FlexILS'."""
        ...

    @property
    @abstractmethod
    def location(self) -> LocationProtocol:
        """The location where the node is housed."""
        ...


class AbcOpticalNodeProvisioning(AbcOpticalNodeInactive, ABC):
    """Base Product Block for Optical Nodes in provisioning state."""

    fqdn: Fqdn
    role: NodeRole
    management_ips: IpAddressesList


class AbcOpticalNode(AbcOpticalNodeProvisioning, ABC):
    """Base Product Block for Optical Nodes in operational state."""

    sw_version: str
