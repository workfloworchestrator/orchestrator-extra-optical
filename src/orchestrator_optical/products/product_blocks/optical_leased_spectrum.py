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
from products.product_blocks.optical_ports import (
    OlsAddDropPortBlock,
    OlsAddDropPortBlockInactive,
    OlsAddDropPortBlockProvisioning,
    OlsLinePortBlock,
    OlsLinePortBlockInactive,
    OlsLinePortBlockProvisioning,
    TrxLineInterfaceBlock,
    TrxLineInterfaceBlockInactive,
    TrxLineInterfaceBlockProvisioning,
)

ListOfPorts = Annotated[list[SI], Len(min_length=2, max_length=2), "List of the 2 ports connected by the fiber."]


InactivePortBlocks = OlsAddDropPortBlockInactive | OlsLinePortBlockInactive | TrxLineInterfaceBlockInactive
ProvisioningPortBlocks = (
    OlsAddDropPortBlockProvisioning | OlsLinePortBlockProvisioning | TrxLineInterfaceBlockProvisioning
)
ActivePortBlocks = OlsAddDropPortBlock | OlsLinePortBlock | TrxLineInterfaceBlock


class LeasedOpticalSpectrumBlockInactive(ProductBlockModel, product_block_name="LeasedOpticalSpectrum"):
    terminations: ListOfPorts[InactivePortBlocks]
    spectrum_name: str | None
    irm_id: str | None


class LeasedOpticalSpectrumBlockProvisioning(
    LeasedOpticalSpectrumBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    terminations: ListOfPorts[ProvisioningPortBlocks]


class LeasedOpticalSpectrumBlock(LeasedOpticalSpectrumBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    terminations: ListOfPorts[ActivePortBlocks]
