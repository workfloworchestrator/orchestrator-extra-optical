"""Workflow execution contracts for Optical Ports."""

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from orchestrator_optical.contracts.optical_nodes import OpticalNodeContract
from orchestrator_optical.contracts.packet_node import PacketNodeContract
from orchestrator_optical.utils.custom_types.frequencies import Passband


@runtime_checkable
class PortContract(Protocol):
    """Base structural contract for any optical port."""

    port_name: str
    port_description: str

    @property
    def host_node(self) -> OpticalNodeContract:
        """The optical node or coherent pluggable hosting the port."""
        ...


@runtime_checkable
class PassbandPortContract(PortContract, Protocol):
    """Contract for optical ports that utilize frequency passbands."""

    used_passbands: Sequence[Passband]


@runtime_checkable
class OlsAddDropPortContract(PassbandPortContract, Protocol):
    """Contract for OLS Add/Drop ports."""


@runtime_checkable
class OlsLinePortContract(PassbandPortContract, Protocol):
    """Contract for OLS Line ports."""


@runtime_checkable
class TrxLineInterfaceContract(PassbandPortContract, Protocol):
    """Contract for Transponder Line Interfaces."""


@runtime_checkable
class TrxClientInterfaceContract(PortContract, Protocol):
    """Contract for Transponder Client Interfaces (No passbands)."""


@runtime_checkable
class CoherentPluggableContract(PassbandPortContract, Protocol):
    """The structural contract for coherent pluggables."""

    fw_version: str

    @property
    def host_node(self) -> PacketNodeContract:
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
