"""Module that defines the contract for location-related data used in optical nodes."""

from typing import Protocol, runtime_checkable

from orchestrator_optical.utils.custom_types.coordinates import LatitudeCoordinate, LongitudeCoordinate


@runtime_checkable
class LocationProtocol(Protocol):
    """Defines the Protocol (contract) of any housing used for Network Nodes.

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
