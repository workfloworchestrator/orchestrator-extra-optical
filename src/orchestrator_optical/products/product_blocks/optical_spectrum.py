"""Module for Optical Spectrum product blocks."""

from orchestrator_optical.abstracts.product_blocks.optical_spectrum import (
    AbstractOpticalSpectrumBlock,
    AbstractOpticalSpectrumBlockInactive,
    AbstractOpticalSpectrumBlockProvisioning,
    OpticalSpectrumSectionsList,
)
from orchestrator_optical.products.product_blocks.spectrum_section import (
    OpticalSpectrumSection,
    OpticalSpectrumSectionInactive,
    OpticalSpectrumSectionProvisioning,
)

# --- Inactive ---


class OpticalSpectrumInactive(AbstractOpticalSpectrumBlockInactive, product_block_name="OpticalSpectrum"):
    """Inactive state of the Optical Spectrum product block."""

    sections: OpticalSpectrumSectionsList[OpticalSpectrumSectionInactive]


# --- Provisioning ---


class OpticalSpectrumProvisioning(OpticalSpectrumInactive, AbstractOpticalSpectrumBlockProvisioning):
    """Provisioning state of the Optical Spectrum product block."""

    sections: OpticalSpectrumSectionsList[OpticalSpectrumSectionProvisioning]


# --- Active ---


class OpticalSpectrum(OpticalSpectrumProvisioning, AbstractOpticalSpectrumBlock):
    """Active state of the Optical Spectrum product block."""

    sections: OpticalSpectrumSectionsList[OpticalSpectrumSection]
