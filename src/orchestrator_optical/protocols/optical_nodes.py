"""Workflow execution contracts for Optical Nodes."""

from collections.abc import Sequence
from enum import StrEnum
from typing import Literal, Protocol, runtime_checkable

from orchestrator_optical.protocols.location import LocationProtocol
from orchestrator_optical.utils.custom_types.fqdn import Fqdn
from orchestrator_optical.utils.custom_types.ip_address import IPAddress


class NodeRole(StrEnum):
    """Device type based on its functionalities. Since chasses are modular, the type can change during device's life."""

    ROADM = "ROADM"
    AMPLIFIER = "Amplifier"
    TRANSPONDER = "Transponder"
    TRANSPONDER_XOADM = "Transponder and xOADM"


@runtime_checkable
class OpticalNodeProtocol(Protocol):
    """Base contract for any optical node."""

    fqdn: Fqdn
    role: NodeRole
    management_ips: Sequence[IPAddress]
    sw_version: str

    @property
    def vendor_and_platform(self) -> str:
        """The vendor and platform of the node, e.g. 'Nokia FlexILS'."""
        ...

    @property
    def location(self) -> LocationProtocol:
        """The location where the node is housed."""
        ...


@runtime_checkable
class NokiaFlexIlsProtocol(OpticalNodeProtocol, Protocol):
    """Specific contract for Nokia FlexILS nodes."""

    role: Literal[NodeRole.ROADM, NodeRole.AMPLIFIER]
    gmpls_id: IPAddress
    vendor: Literal["Nokia"]
    platform: Literal["FlexILS"]
