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
    TrxClientInterfaceBlock,
    TrxClientInterfaceBlockInactive,
    TrxClientInterfaceBlockProvisioning,
)

from orchestrator_optical.products.product_blocks.optical_transport_channel import (
    OpticalTransportChannelBlock,
    OpticalTransportChannelBlockInactive,
    OpticalTransportChannelBlockProvisioning,
)

ListOfClient_ports = Annotated[list[SI], Len(min_length=2, max_length=2)]

ListOfTransport_channels = Annotated[list[SI], Len(min_length=1, max_length=2)]



class OpticalDigitalServiceBlockInactive(
    ProductBlockModel, product_block_name="OpticalDigitalService"
):
    service_id: str | None = None
    service_name: str | None = None
    client_ports: ListOfClient_ports[TrxClientInterfaceBlockInactive]
    transport_channels: ListOfTransport_channels[OpticalTransportChannelBlockInactive]


class OpticalDigitalServiceBlockProvisioning(
    OpticalDigitalServiceBlockInactive, lifecycle=[SubscriptionLifecycle.PROVISIONING]
):
    service_id: str
    service_name: str
    client_ports: ListOfClient_ports[TrxClientInterfaceBlockProvisioning]
    transport_channels: ListOfTransport_channels[
        OpticalTransportChannelBlockProvisioning
    ]


class OpticalDigitalServiceBlock(
    OpticalDigitalServiceBlockProvisioning, lifecycle=[SubscriptionLifecycle.ACTIVE]
):
    service_id: str
    service_name: str
    client_ports: ListOfClient_ports[TrxClientInterfaceBlock]
    transport_channels: ListOfTransport_channels[OpticalTransportChannelBlock]
