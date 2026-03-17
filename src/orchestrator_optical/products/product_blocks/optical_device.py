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


from abc import ABC, abstractmethod
from enum import StrEnum
from typing import Self

from orchestrator.domain.base import ProductBlockModel
from orchestrator.types import SubscriptionLifecycle
from pydantic import model_validator

from orchestrator_optical.utils.custom_types.fqdn import FQDN
from orchestrator_optical.utils.custom_types.ip_address import IPAddress


class DeviceType(StrEnum):
    """Device type based on its functionalities. Since chasses are modular, the type can change during device life."""

    ROADM = "ROADM"
    Amplifier = "Amplifier"
    Transponder = "Transponder"
    Transceiver = "Transceiver"
    TransponderAndOADM = "Transponder+OADM"


class OpticalDeviceBlockInactive(ProductBlockModel, ABC, product_block_name="OpticalDevice"):
    fqdn: FQDN | None = None
    device_type: DeviceType | None = None
    loopback_ip: IPAddress | None = None
    management_ip: IPAddress | None = None
    irm_id: str | None

    @property
    @abstractmethod
    def location(self):
        msg = f"Class {self.__class__.__name__} must be subclassed to set custom properties."
        raise NotImplementedError(msg)  # FIXME


class OpticalDeviceBlockProvisioning(OpticalDeviceBlockInactive, ABC, lifecycle=[SubscriptionLifecycle.PROVISIONING]):
    fqdn: FQDN
    device_type: DeviceType

    @model_validator(mode="after")
    def validate_ip(self) -> Self:
        if self.loopback_ip is None and self.management_ip is None:
            msg = "At least one of loopback and management IPs must be provided."
            raise ValueError(msg)


class OpticalDeviceBlock(OpticalDeviceBlockProvisioning, ABC, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    device_type: DeviceType
