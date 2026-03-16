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
from orchestrator.types import SubscriptionLifecycle

from orchestrator_optical.products.product_blocks.optical_device import (
    OpticalDeviceBlock,
    OpticalDeviceBlockInactive,
    OpticalDeviceBlockProvisioning,
)
from orchestrator_optical.utils.custom_types.frequencies import Passband

# --- Types ---

ListOfPassbands = Annotated[list[Passband], Len(min_length=0, max_length=128), "List of used passbands (MHz, MHz)."]

# --- Abstract Base Hierarchies ---
# We use these to encapsulate the lifecycle field transitions.
# These are not assigned a 'product_block_name' so they remain internal templates.


class _PortInactive(ProductBlockModel):
    optical_device: OpticalDeviceBlockInactive | None = None
    port_name: str | None = None
    port_description: str | None = None


class _PortProvisioning(_PortInactive):
    optical_device: OpticalDeviceBlockProvisioning
    port_name: str


class _PortActive(_PortProvisioning):
    optical_device: OpticalDeviceBlock


class _PassbandPortInactive(_PortInactive):
    used_passbands: ListOfPassbands | None = None


class _PassbandPortProvisioning(_PassbandPortInactive, _PortProvisioning):
    used_passbands: ListOfPassbands


class _PassbandPortActive(_PassbandPortProvisioning, _PortActive):
    pass


# --- Concrete Product Blocks ---


# OpticalPort
class OpticalPortBlockInactive(_PassbandPortInactive, product_block_name="OpticalPort"):
    pass


class OpticalPortBlockProvisioning(
    OpticalPortBlockInactive, _PassbandPortProvisioning, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    pass


class OpticalPortBlock(OpticalPortBlockProvisioning, _PassbandPortActive, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    pass


# OlsAddDropPort
class OlsAddDropPortBlockInactive(_PassbandPortInactive, product_block_name="OlsAddDropPort"):
    pass


class OlsAddDropPortBlockProvisioning(
    OlsAddDropPortBlockInactive, _PassbandPortProvisioning, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    pass


class OlsAddDropPortBlock(
    OlsAddDropPortBlockProvisioning, _PassbandPortActive, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    pass


# OlsLinePort
class OlsLinePortBlockInactive(_PassbandPortInactive, product_block_name="OlsLinePort"):
    pass


class OlsLinePortBlockProvisioning(
    OlsLinePortBlockInactive, _PassbandPortProvisioning, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    pass


class OlsLinePortBlock(OlsLinePortBlockProvisioning, _PassbandPortActive, lifecycle=[SubscriptionLifecycle.ACTIVE]):
    pass


# TrxLineInterface
class TrxLineInterfaceBlockInactive(_PassbandPortInactive, product_block_name="TrxLineInterface"):
    pass


class TrxLineInterfaceBlockProvisioning(
    TrxLineInterfaceBlockInactive, _PassbandPortProvisioning, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    pass


class TrxLineInterfaceBlock(
    TrxLineInterfaceBlockProvisioning, _PassbandPortActive, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    pass


# TrxClientInterface (Does NOT have used_passbands)
class TrxClientInterfaceBlockInactive(_PortInactive, product_block_name="TrxClientInterface"):
    pass


class TrxClientInterfaceBlockProvisioning(
    TrxClientInterfaceBlockInactive, _PortProvisioning, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    pass


class TrxClientInterfaceBlock(
    TrxClientInterfaceBlockProvisioning, _PortActive, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    pass
