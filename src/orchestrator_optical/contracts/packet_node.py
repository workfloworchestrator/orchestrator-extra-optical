"""Module that defines the contract for packet nodes hosting coherent pluggables."""

from typing import Protocol, runtime_checkable

from orchestrator_optical.products.product_types.optical_nodes.base import LocationContract
from orchestrator_optical.utils.custom_types.fqdn import Fqdn
from orchestrator_optical.utils.custom_types.ip_address import IPAddress


@runtime_checkable
class PacketNodeContract(Protocol):
    """Defines the Protocol (contract) of any packet node hosting a coherent pluggable.

    The optical orchestrator workflows will rely on these.
    """

    @property
    def management_ips(self) -> list[IPAddress]:
        """List of management IP addresses of the host device."""
        ...

    @property
    def fqdn(self) -> Fqdn | None:
        """The FQDN of the host device."""
        ...

    @property
    def vendor(self) -> str | None:
        """The vendor of the host device."""
        ...

    @property
    def model(self) -> str | None:
        """The model of the host device."""
        ...

    @property
    def sw_version(self) -> str | None:
        """The software version of the host device."""
        ...

    @property
    def location(self) -> LocationContract:
        """The location where the node is housed."""
        ...
