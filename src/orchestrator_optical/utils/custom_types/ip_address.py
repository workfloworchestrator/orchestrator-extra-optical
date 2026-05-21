# 

"""IP addresses. Copied from GEANT Service Orchestrator project."""

import ipaddress
from typing import Annotated, Any

from pydantic import AfterValidator, Field, PlainSerializer
from pydantic_forms.types import strEnum
from typing_extensions import Doc


def validate_ipv4_or_ipv6(value: str) -> str:
    """Validate that a value is a valid IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(value)
    except ValueError as e:
        msg = "Enter a valid IPv4 or IPv6 address."
        raise ValueError(msg) from e
    else:
        return value


def validate_ipv4_or_ipv6_network(value: str) -> str:
    """Validate that a value is a valid IPv4 or IPv6 network."""
    try:
        ipaddress.ip_network(value)
    except ValueError as e:
        msg = "Enter a valid IPv4 or IPv6 network."
        raise ValueError(msg) from e
    else:
        return value


def _str(value: Any) -> str:
    return str(value)


IPv4AddressType = Annotated[ipaddress.IPv4Address, PlainSerializer(_str, return_type=str, when_used="always")]
IPv4NetworkType = Annotated[ipaddress.IPv4Network, PlainSerializer(_str, return_type=str, when_used="always")]
IPv6AddressType = Annotated[ipaddress.IPv6Address, PlainSerializer(_str, return_type=str, when_used="always")]
IPv6NetworkType = Annotated[ipaddress.IPv6Network, PlainSerializer(_str, return_type=str, when_used="always")]
IPAddress = Annotated[str, AfterValidator(validate_ipv4_or_ipv6)]
IPNetwork = Annotated[str, AfterValidator(validate_ipv4_or_ipv6_network)]
IPV4Netmask = Annotated[int, Field(ge=0, le=32), Doc("A valid netmask for an IPv4 network or address.")]
IPV6Netmask = Annotated[int, Field(ge=0, le=128), Doc("A valid netmask for an IPv6 network or address.")]
PortNumber = Annotated[
    int,
    Field(
        gt=0,
        le=49151,
    ),
    Doc(
        "Constrained integer for valid port numbers. The range from 49152 to 65535 is marked as ephemeral, "
        "and can therefore not be selected for permanent allocation."
    ),
]


class AddressSpace(strEnum):
    """Types of address space. Can be private or public."""

    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"
