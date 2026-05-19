"""Workflow execution contracts for Optical Ports."""

from collections.abc import Sequence
from enum import StrEnum
from typing import Protocol, runtime_checkable

from dotenv.variables import Literal

from orchestrator_optical.protocols.optical_nodes import OpticalNodeProtocol
from orchestrator_optical.protocols.packet_node import PacketNodeProtocol
from orchestrator_optical.utils.custom_types.frequencies import Passband


class PortRole(StrEnum):
    """Device type based on its functionalities. Since chasses are modular, the type can change during device's life."""

    OLS_ADD_DROP = "Optical Line System Add/Drop"
    OLS_LINE = "Optical Line System Line"
    TRANSPONDER_CLIENT = "Transponder Client"
    TRANSPONDER_LINE = "Transponder Line"
    COHERENT_PLUGGABLE = "Coherent Pluggable"


@runtime_checkable
class PortProtocol(Protocol):
    """Base structural contract for any optical port."""

    port_name: str
    port_description: str
    port_role: PortRole

    @property
    def host_node(self) -> OpticalNodeProtocol:
        """The optical node or coherent pluggable hosting the port."""
        ...


@runtime_checkable
class PassbandPortProtocol(PortProtocol, Protocol):
    """Protocol for optical ports that utilize frequency passbands."""

    used_passbands: Sequence[Passband]


@runtime_checkable
class OlsAddDropPortProtocol(PassbandPortProtocol, Protocol):
    """Protocol for OLS Add/Drop ports."""

    port_role: Literal[PortRole.OLS_ADD_DROP] = PortRole.OLS_ADD_DROP


@runtime_checkable
class OlsLinePortProtocol(PassbandPortProtocol, Protocol):
    """Protocol for OLS Line ports."""

    port_role: Literal[PortRole.OLS_LINE] = PortRole.OLS_LINE


@runtime_checkable
class TrxLineInterfaceProtocol(PassbandPortProtocol, Protocol):
    """Protocol for Transponder Line Interfaces."""

    port_role: Literal[PortRole.TRANSPONDER_LINE] = PortRole.TRANSPONDER_LINE


@runtime_checkable
class TrxClientInterfaceProtocol(PortProtocol, Protocol):
    """Protocol for Transponder Client Interfaces (No passbands)."""

    port_role: Literal[PortRole.TRANSPONDER_CLIENT] = PortRole.TRANSPONDER_CLIENT


@runtime_checkable
class CoherentPluggableProtocol(PassbandPortProtocol, Protocol):
    """The structural contract for coherent pluggables."""

    port_role: Literal[PortRole.COHERENT_PLUGGABLE] = PortRole.COHERENT_PLUGGABLE
    fw_version: str

    @property
    def host_node(self) -> PacketNodeProtocol:
        """The packet node device hosting the pluggable."""
        ...

    @property
    def vendor(self) -> str:
        """The vendor of the pluggable."""
        ...

    @property
    def part_number(self) -> str:
        """The part number of the pluggable."""
        ...
