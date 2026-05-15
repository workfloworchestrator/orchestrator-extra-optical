"""Module for Optical Fiber product blocks."""

from abc import ABC
from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_ports import (
    AbstractOlsAddDropPortBlock,
    AbstractOlsAddDropPortBlockInactive,
    AbstractOlsAddDropPortBlockProvisioning,
    AbstractOlsLinePortBlock,
    AbstractOlsLinePortBlockInactive,
    AbstractOlsLinePortBlockProvisioning,
    AbstractTrxClientInterfaceBlock,
    AbstractTrxClientInterfaceBlockInactive,
    AbstractTrxClientInterfaceBlockProvisioning,
    AbstractTrxLineInterfaceBlock,
    AbstractTrxLineInterfaceBlockInactive,
    AbstractTrxLineInterfaceBlockProvisioning,
)

# --- Types ---

ListOfPorts = Annotated[list[SI], Len(min_length=2, max_length=2), "List of the 2 ports connected by the fiber."]

# Patch Port Blocks: trx client, trx line, ols add/drop ports
InactivePatchPortBlocks = (
    AbstractTrxClientInterfaceBlockInactive
    | AbstractTrxLineInterfaceBlockInactive
    | AbstractOlsAddDropPortBlockInactive
)
ProvisioningPatchPortBlocks = (
    AbstractTrxClientInterfaceBlockProvisioning
    | AbstractTrxLineInterfaceBlockProvisioning
    | AbstractOlsAddDropPortBlockProvisioning
)
ActivePatchPortBlocks = AbstractTrxClientInterfaceBlock | AbstractTrxLineInterfaceBlock | AbstractOlsAddDropPortBlock

# Span Port Blocks: only ols line ports
InactiveSpanPortBlocks = AbstractOlsLinePortBlockInactive
ProvisioningSpanPortBlocks = AbstractOlsLinePortBlockProvisioning
ActiveSpanPortBlocks = AbstractOlsLinePortBlock


# Leased Spectrum Port Blocks: trx line, ols add/drop ports, ols line ports
InactiveLeasedSpectrumPortBlocks = (
    AbstractTrxLineInterfaceBlockInactive | AbstractOlsAddDropPortBlockInactive | AbstractOlsLinePortBlockInactive
)
ProvisioningLeasedSpectrumPortBlocks = (
    AbstractTrxLineInterfaceBlockProvisioning
    | AbstractOlsAddDropPortBlockProvisioning
    | AbstractOlsLinePortBlockProvisioning
)
ActiveLeasedSpectrumPortBlocks = AbstractTrxLineInterfaceBlock | AbstractOlsAddDropPortBlock | AbstractOlsLinePortBlock

# --- Abstract Base Hierarchies ---
# We use these to encapsulate the lifecycle field transitions.


class AbstractFiberInactive(ABC, ProductBlockModel):
    """Abstract base class for inactive fibers."""

    fiber_name: str | None = None


class AbstractFiberProvisioning(ABC, AbstractFiberInactive):
    """Abstract base class for provisioning fibers."""

    fiber_name: str


class AbstractFiberActive(ABC, AbstractFiberProvisioning):
    """Abstract base class for active fibers."""


# --- Abstract Product Blocks ---


# OpticalPatch
class AbstractOpticalPatchBlockInactive(ABC, AbstractFiberInactive):
    """Abstract base class for inactive OpticalPatch product blocks."""

    terminations: ListOfPorts[InactivePatchPortBlocks]


class AbstractOpticalPatchBlockProvisioning(
    ABC,
    AbstractOpticalPatchBlockInactive,
    AbstractFiberProvisioning,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base class for provisioning OpticalPatch product blocks."""

    terminations: ListOfPorts[ProvisioningPatchPortBlocks]


class AbstractOpticalPatchBlock(
    ABC, AbstractOpticalPatchBlockProvisioning, AbstractFiberActive, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active OpticalPatch product blocks."""

    terminations: ListOfPorts[ActivePatchPortBlocks]


# OpticalSpan
class AbstractOpticalSpanBlockInactive(ABC, AbstractFiberInactive):
    """Abstract base class for inactive OpticalSpan product blocks."""

    terminations: ListOfPorts[InactiveSpanPortBlocks]


class AbstractOpticalSpanBlockProvisioning(
    ABC,
    AbstractOpticalSpanBlockInactive,
    AbstractFiberProvisioning,
    lifecycle=[SubscriptionLifecycle.PROVISIONING],
):
    """Abstract base class for provisioning OpticalSpan product blocks."""

    terminations: ListOfPorts[ProvisioningSpanPortBlocks]


class AbstractOpticalSpanBlock(
    ABC, AbstractOpticalSpanBlockProvisioning, AbstractFiberActive, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active OpticalSpan product blocks."""

    terminations: ListOfPorts[ActiveSpanPortBlocks]


# OpticalLeasedSpectrum
class AbstractLeasedSpectrumBlockInactive(ABC, ProductBlockModel):
    """Abstract base class for inactive leased spectrum."""

    leased_spectrum_name: str | None = None
    terminations: ListOfPorts[InactiveLeasedSpectrumPortBlocks]


class AbstractLeasedSpectrumBlockProvisioning(ABC, AbstractLeasedSpectrumBlockInactive):
    """Abstract base class for provisioning leased spectrum."""

    leased_spectrum_name: str
    terminations: ListOfPorts[ProvisioningLeasedSpectrumPortBlocks]


class AbstractLeasedSpectrumBlockActive(ABC, AbstractLeasedSpectrumBlockProvisioning):
    """Abstract base class for active leased spectrum."""

    terminations: ListOfPorts[ActiveLeasedSpectrumPortBlocks]
