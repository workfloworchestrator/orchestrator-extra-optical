"""Abstract classes for OpticalSpectrum product blocks."""

from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle

from orchestrator_optical.abstracts.product_blocks.optical_spectrum_section import (
    AbstractOpticalSpectrumSectionBlock,
    AbstractOpticalSpectrumSectionBlockInactive,
    AbstractOpticalSpectrumSectionBlockProvisioning,
)
from orchestrator_optical.utils.custom_types.frequencies import Passband

OpticalSpectrumSectionsList = Annotated[list[SI], Len(min_length=0, max_length=9)]


class AbstractOpticalSpectrumBlockInactive(ProductBlockModel):
    """Abstract class for inactive Optical Spectrum product blocks."""

    spectrum_name: str | None = None
    passband: Passband | None = None
    sections: OpticalSpectrumSectionsList[AbstractOpticalSpectrumSectionBlockInactive]


class AbstractOpticalSpectrumBlockProvisioning(
    AbstractOpticalSpectrumBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    """Abstract class for provisioning Optical Spectrum product blocks."""

    spectrum_name: str | None = None
    passband: Passband
    sections: OpticalSpectrumSectionsList[AbstractOpticalSpectrumSectionBlockProvisioning]


class AbstractOpticalSpectrumBlock(AbstractOpticalSpectrumBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    """Abstract class for active Optical Spectrum product blocks."""

    spectrum_name: str
    passband: Passband
    sections: OpticalSpectrumSectionsList[AbstractOpticalSpectrumSectionBlock]
