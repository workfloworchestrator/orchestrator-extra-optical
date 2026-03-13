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


from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_extra_optical.products.product_blocks.optical_dummy_router import (
    RouterBlock,
    RouterBlockInactive,
    RouterBlockProvisioning,
)


class CoherentPluggableBlockInactive(ProductBlockModel, product_block_name="CoherentPluggable"):
    host_device: RouterBlockInactive
    port_name: str | None = None


class CoherentPluggableBlockProvisioning(
    CoherentPluggableBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    host_device: RouterBlockProvisioning
    port_name: str


class CoherentPluggableBlock(CoherentPluggableBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    host_device: RouterBlock
