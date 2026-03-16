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

from enum import StrEnum

from orchestrator.domain.base import SubscriptionModel
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_device import (
    OpticalDeviceBlock,
    OpticalDeviceBlockInactive,
    OpticalDeviceBlockProvisioning,
)


class DeviceModel(StrEnum):
    NOKIA_GROOVE_G30 = "Nokia Groove G30"
    NOKIA_FLEXILS = "Nokia FlexILS"
    NOKIA_GX_G42 = "Nokia GX G42"

class OpticalDeviceInactive(SubscriptionModel, is_base=True):
    device_model = DeviceModel
    optical_device: OpticalDeviceBlockInactive


class OpticalDeviceProvisioning(
    OpticalDeviceInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    device_model = DeviceModel
    optical_device: OpticalDeviceBlockProvisioning


class OpticalDevice(
    OpticalDeviceProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    device_model = DeviceModel
    optical_device: OpticalDeviceBlock
