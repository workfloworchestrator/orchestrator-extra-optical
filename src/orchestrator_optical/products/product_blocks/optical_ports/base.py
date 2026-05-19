from orchestrator_optical.protocols.packet_node import PacketNodeProtocol
from orchestrator_optical.product_blocks.optical_nodes.base import AbcOpticalNode
from pydantic import computed_field
from abc import ABC, abstractmethod
from collections.abc import Sequence
from enum import StrEnum
from typing import Literal, Protocol, runtime_checkable

from orchestrator.domain.base import ProductBlock
from pydantic import Field

from orchestrator_optical.protocols.location import LocationProtocol
from orchestrator_optical.utils.custom_types.fqdn import Fqdn
from orchestrator_optical.utils.custom_types.ip_address import IPAddress


class PortRole(StrEnum):
    """Device type based on its functionalities. Since chasses are modular, the type can change during device's life."""

    OLS_ADD_DROP = "Optical Line System Add/Drop"
    OLS_LINE = "Optical Line System Line"
    TRANSPONDER_CLIENT = "Transponder Client"
    TRANSPONDER_LINE = "Transponder Line"
    COHERENT_PLUGGABLE = "Coherent Pluggable"


NotCoherentPluggablePortRole = Literal[
    PortRole.OLS_ADD_DROP,
    PortRole.OLS_LINE,
    PortRole.TRANSPONDER_CLIENT,
    PortRole.TRANSPONDER_LINE,
]


class AbcOpticalPort(ProductBlock, ABC):
    """Abstract Product Block for Optical Ports."""

    role: NotCoherentPluggablePortRole | None = Field(None, description="The role of the port.")
    port_name: str | None
    port_description: str | None

    @property
    @abstractmethod
    def host_node(self) -> AbcOpticalNode:
        """The node hosting the port."""
        ...


class AbcCoherentPluggable(AbcOpticalPort, ABC):
    """Abstract Product Block for Coherent Pluggables."""

    role: PortRole.COHERENT_PLUGGABLE = PortRole.COHERENT_PLUGGABLE
    fw_version: str | None = Field(None, description="The software version of the pluggable.")

    @property
    @abstractmethod
    def host_node(self) -> PacketNodeProtocol:
        """The packet node hosting the pluggable."""
        ...

    @property
    @abstractmethod
    def vendor(self) -> str:
        """The vendor of the pluggable."""
        ...

    @property
    @abstractmethod
    def part_number(self) -> str:
        """The part number of the pluggable."""
        ...
