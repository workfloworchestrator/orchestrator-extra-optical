# Copyright 2025 GARR.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SI, SubscriptionLifecycle
from pydantic import Field

from orchestrator_optical.products.product_blocks.optical_spectrum_section import (
    OpticalSpectrumSectionBlock,
    OpticalSpectrumSectionBlockInactive,
    OpticalSpectrumSectionBlockProvisioning,
)
from orchestrator_optical.utils.custom_types.frequencies import Passband

SectionsList = Annotated[
    list[SI],
    Len(min_length=0, max_length=9),
    "ordered list of single-platform-OLS sections that make up the end-to-end optical connection.",
]


class OpticalSpectrumBlockInactive(ProductBlockModel, product_block_name="OpticalSpectrum"):
    spectrum_name: str | None = None
    passband: Passband | None = None
    sections: SectionsList[OpticalSpectrumSectionBlockInactive] = Field(default_factory=list)


class OpticalSpectrumBlockProvisioning(OpticalSpectrumBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]):
    spectrum_name: str | None = None
    passband: Passband
    sections: SectionsList[OpticalSpectrumSectionBlockProvisioning]


class OpticalSpectrumBlock(OpticalSpectrumBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    spectrum_name: str
    passband: Passband
    sections: SectionsList[OpticalSpectrumSectionBlock]
