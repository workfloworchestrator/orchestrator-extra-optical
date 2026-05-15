"""Module for Optical Spectrum product blocks."""

from abc import ABC
from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_spectrum_section import (
    AbstractOpticalSpectrumSectionBlock,
    AbstractOpticalSpectrumSectionBlockInactive,
    AbstractOpticalSpectrumSectionBlockProvisioning,
)
from orchestrator_optical.products.product_blocks.utils.custom_types.frequencies import Passband

OpticalSpectrumSectionsList = Annotated[list[SI], Len(min_length=0, max_length=9)]


class AbstractOpticalSpectrumBlockInactive(ABC, ProductBlockModel):
    """Abstract base class for inactive Optical Spectrum product blocks."""

    spectrum_name: str | None = None
    passband: Passband | None = None
    sections: OpticalSpectrumSectionsList[AbstractOpticalSpectrumSectionBlockInactive]


class AbstractOpticalSpectrumBlockProvisioning(
    ABC, AbstractOpticalSpectrumBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """Abstract base class for provisioning Optical Spectrum product blocks."""

    spectrum_name: str | None = None
    passband: Passband
    sections: OpticalSpectrumSectionsList[AbstractOpticalSpectrumSectionBlockProvisioning]


class AbstractOpticalSpectrumBlock(
    ABC, AbstractOpticalSpectrumBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    """Abstract base class for active Optical Spectrum product blocks."""

    spectrum_name: str
    passband: Passband
    sections: OpticalSpectrumSectionsList[AbstractOpticalSpectrumSectionBlock]
