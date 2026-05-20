"""Module for Optical Port product blocks."""

from enum import StrEnum
from typing import Annotated, Literal

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.abstracts.product_blocks.optical_node import (
    AbstractOpticalNodeBlock,
    AbstractOpticalNodeBlockInactive,
    AbstractOpticalNodeBlockProvisioning,
)
from orchestrator_optical.utils.custom_types.frequencies import Passband

# --- Types & Enums ---

ListOfPassbands = Annotated[list[Passband], Len(min_length=0, max_length=128), "List of used passbands (MHz, MHz)."]


class PortRole(StrEnum):
    """missing docstring."""

    OLS_ADD_DROP = "Optical Line System Add/Drop"
    OLS_LINE = "Optical Line System Line"
    TRANSPONDER_CLIENT = "Transponder Client"
    TRANSPONDER_LINE = "Transponder Line"
    COHERENT_PLUGGABLE = "Coherent Pluggable"


# --- Inactive ---


class _PortInactive(ProductBlockModel):
    """missing docstring."""

    role: PortRole | None = None
    port_name: str | None = None
    port_description: str | None = None
    host_node: AbstractOpticalNodeBlockInactive


class AbstractOlsAddDropPortBlockInactive(_PortInactive):
    """missing docstring."""

    role: Literal[PortRole.OLS_ADD_DROP] = PortRole.OLS_ADD_DROP
    passbands: ListOfPassbands | None = None
    host_node: AbstractOpticalNodeBlockInactive


class AbstractOlsLinePortBlockInactive(_PortInactive):
    """missing docstring."""

    role: Literal[PortRole.OLS_LINE] = PortRole.OLS_LINE
    passbands: ListOfPassbands | None = None
    host_node: AbstractOpticalNodeBlockInactive


class AbstractTransponderClientPortBlockInactive(_PortInactive):
    """missing docstring."""

    role: Literal[PortRole.TRANSPONDER_CLIENT] = PortRole.TRANSPONDER_CLIENT
    host_node: AbstractOpticalNodeBlockInactive


class AbstractTransponderLinePortBlockInactive(_PortInactive):
    """missing docstring."""

    role: Literal[PortRole.TRANSPONDER_LINE] = PortRole.TRANSPONDER_LINE
    host_node: AbstractOpticalNodeBlockInactive


# --- Provisioning ---


class _PortProvisioning(_PortInactive, lifecycle=SubscriptionLifecycle.PROVISIONING):
    """missing docstring."""

    role: PortRole
    port_name: str
    host_node: AbstractOpticalNodeBlockProvisioning


class AbstractOlsAddDropPortBlockProvisioning(_PortProvisioning, lifecycle=SubscriptionLifecycle.PROVISIONING):
    """missing docstring."""

    role: Literal[PortRole.OLS_ADD_DROP] = PortRole.OLS_ADD_DROP
    passbands: ListOfPassbands
    host_node: AbstractOpticalNodeBlockProvisioning


class AbstractOlsLinePortBlockProvisioning(_PortProvisioning, lifecycle=SubscriptionLifecycle.PROVISIONING):
    """missing docstring."""

    role: Literal[PortRole.OLS_LINE] = PortRole.OLS_LINE
    passbands: ListOfPassbands
    host_node: AbstractOpticalNodeBlockProvisioning


class AbstractTransponderClientPortBlockProvisioning(_PortProvisioning, lifecycle=SubscriptionLifecycle.PROVISIONING):
    """missing docstring."""

    role: Literal[PortRole.TRANSPONDER_CLIENT] = PortRole.TRANSPONDER_CLIENT
    host_node: AbstractOpticalNodeBlockProvisioning


class AbstractTransponderLinePortBlockProvisioning(_PortProvisioning, lifecycle=SubscriptionLifecycle.PROVISIONING):
    """missing docstring."""

    role: Literal[PortRole.TRANSPONDER_LINE] = PortRole.TRANSPONDER_LINE
    host_node: AbstractOpticalNodeBlockProvisioning


# --- Active ---


class _Port(_PortProvisioning, lifecycle=SubscriptionLifecycle.ACTIVE):
    """missing docstring."""

    port_description: str
    host_node: AbstractOpticalNodeBlock


class AbstractOlsAddDropPortBlock(_Port, lifecycle=SubscriptionLifecycle.ACTIVE):
    """missing docstring."""

    role: Literal[PortRole.OLS_ADD_DROP] = PortRole.OLS_ADD_DROP
    passbands: ListOfPassbands
    host_node: AbstractOpticalNodeBlock


class AbstractOlsLinePortBlock(_Port, lifecycle=SubscriptionLifecycle.ACTIVE):
    """missing docstring."""

    role: Literal[PortRole.OLS_LINE] = PortRole.OLS_LINE
    passbands: ListOfPassbands
    host_node: AbstractOpticalNodeBlock


class AbstractTransponderClientPortBlock(_Port, lifecycle=SubscriptionLifecycle.ACTIVE):
    """missing docstring."""

    role: Literal[PortRole.TRANSPONDER_CLIENT] = PortRole.TRANSPONDER_CLIENT
    host_node: AbstractOpticalNodeBlock


class AbstractTransponderLinePortBlock(_Port, lifecycle=SubscriptionLifecycle.ACTIVE):
    """missing docstring."""

    role: Literal[PortRole.TRANSPONDER_LINE] = PortRole.TRANSPONDER_LINE
    host_node: AbstractOpticalNodeBlock
