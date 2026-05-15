"""Module that defines the contract for location-related data used in optical nodes."""

from typing import Annotated, Protocol, runtime_checkable

from annotated_types import Len

from orchestrator_optical.utils.custom_types.coordinates import LatitudeCoordinate, LongitudeCoordinate
from orchestrator_optical.utils.custom_types.ip_address import IPAddress

IpAddressesList = Annotated[
    list[IPAddress], Len(min_length=1, max_length=10), "List of the management IP addresses of the device."
]


@runtime_checkable
class LocationContract(Protocol):
    """Defines the Protocol (contract) of any housing used for Optical Nodes.

    The optical orchestrator workflows will rely on these.
    """

    @property
    def latitude(self) -> LatitudeCoordinate | None:
        """The latitude coordinate of the location."""
        ...

    @property
    def longitude(self) -> LongitudeCoordinate | None:
        """The longitude coordinate of the location."""
        ...

    @property
    def fqdn_subdomain(self) -> str:
        """The subdomain of the housing location that is used in the FQDN of the devices.

        For example, for the FQDN `router1.roomA.pop42.myorg.net`, the subdomain of the location is `roomA.pop42`
        """
        ...
