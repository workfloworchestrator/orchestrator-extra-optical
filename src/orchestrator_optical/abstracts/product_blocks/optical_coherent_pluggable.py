"""Module for Optical Port product blocks."""

from abc import ABC, abstractmethod
from typing import Literal

from orchestrator.domain.context_cache import get_from_cache
from pydantic import computed_field

from orchestrator_optical.abstracts.product_blocks.optical_port import (
    AbstractOpticalPortBlock,
    AbstractOpticalPortBlockProvisioning,
    PortRole,
    _PortInactive,
)
from orchestrator_optical.protocols.packet_node import PacketNodeProtocol


class AbstractCoherentPluggableBlockInactive(_PortInactive, ABC):
    """Abstract base class for inactive CoherentPluggable product blocks."""

    role: Literal[PortRole.COHERENT_PLUGGABLE] = PortRole.COHERENT_PLUGGABLE
    fw_version: str | None = None

    @property
    @abstractmethod
    def host_node(self) -> PacketNodeProtocol | None:
        """The packet node housing the pluggable MUST be implemented as a **field** in the concrete implementation."""
        ...

    @computed_field
    @property
    def vendor_part_number(self) -> str:
        """From fixed_inputs."""
        # Tier 1: Query the domain model context cache (Fastest, 0 DB queries)
        cached_sub = get_from_cache(self.subscription_id)
        if cached_sub:
            return cached_sub.vendor_part_number

        # Tier 2: Scan pre-loaded SQLAlchemy relationship (Prevents N+1 queries)
        if self.subscription and self.subscription.product:
            for fi in self.subscription.product.fixed_inputs:
                if fi.name == "vendor_part_number":
                    return fi.value

        msg = f"Fixed input 'vendor_part_number' not found for subscription {self.owner_subscription_id}"
        raise ValueError(msg)


class AbstractCoherentPluggableBlockProvisioning(
    AbstractCoherentPluggableBlockInactive, AbstractOpticalPortBlockProvisioning, ABC
):
    """Abstract base class for provisioning CoherentPluggable product blocks."""

    fw_version: str

    @property
    @abstractmethod
    def host_node(self) -> PacketNodeProtocol:
        """The packet node housing the pluggable MUST be implemented as a **field** in the concrete implementation."""
        ...


class AbstractCoherentPluggableBlock(AbstractCoherentPluggableBlockProvisioning, AbstractOpticalPortBlock, ABC):
    """Abstract base class for active CoherentPluggable product blocks."""

    @property
    @abstractmethod
    def host_node(self) -> PacketNodeProtocol:
        """The packet node housing the pluggable MUST be implemented as a **field** in the concrete implementation."""
        ...
