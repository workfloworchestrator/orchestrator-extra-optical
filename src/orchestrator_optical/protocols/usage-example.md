## 1. Define the Contract (The Protocol)
Defines the *minimum* properties a block must have.

```python
from typing import Protocol, runtime_checkable

from orchestrator_optical.protocols.location import LocationProtocol
from orchestrator_optical.utils.custom_types.fqdn import Fqdn
from orchestrator_optical.utils.custom_types.ip_address import IPAddress


@runtime_checkable
class PacketNodeProtocol(Protocol):
    """Defines the Protocol of any packet node hosting a coherent pluggable.

    The optical orchestrator workflow steps will rely on these.
    """

    @property
    def management_ips(self) -> list[IPAddress]:
        """List of management IP addresses of the host device."""
        ...

    @property
    def fqdn(self) -> Fqdn | None:
        """The FQDN of the host device."""
        ...

    @property
    def vendor(self) -> str | None:
        """The vendor of the host device."""
        ...

    @property
    def model(self) -> str | None:
        """The model of the host device."""
        ...

    @property
    def sw_version(self) -> str | None:
        """The software version of the host device."""
        ...

    @property
    def location(self) -> LocationProtocol:
        """The location where the node is housed."""
        ...

```

## 2. Define workfloworchestrator-agnostic logic
This function doesn't know what `orchestrator-core` or Pydantic is.

```python
from orchestrator_optical.protocols.packet_node import PacketNodeProtocol
from orchestrator.utils.attributedispatch import attributesingledispatch, attribute_dispatch_base

@attributesingledispatch(discriminators=["vendor", "model", "sw_version"])
def get_name_of_ports_with_coherent_pluggable(packet_node: PacketNodeProtocol) -> list[str]:
    return attribute_dispatch_base(
        get_name_of_ports_with_coherent_pluggable,
        ["vendor", "model", "sw_version"],
        [packet_node.vendor, packet_node.model, packet_node.sw_version],
    )


@get_name_of_ports_with_coherent_pluggable.register("Nokia", "7750 SR-s", "23.10.R2")
def _unique_name_for_tracebacks(packet_node: PacketNodeProtocol) -> list[str]:
    """Pure logic depending only on the Protocol."""
    client = get_client(packet_node) # uses vendor, model, sw_version, and management_ips or fqdn
    # for example, use RESTCONF/NETCONF call returning device-specific port objects
    ports = client.data.chassis.ports.retrieve(depth=2) 
    return [port.name for port in ports if "ZR+" in port.actual_pluggable_type]

# register other implementation based on vendor, model, release version.
```

## 3. Use the Protocol in Workflow Steps
Dynamically load the concrete model, extract the block, and pass it to the Protocol function.

```python
from uuid import UUID
from orchestrator.types import State
from orchestrator.workflow import step
from orchestrator.domain.base import SubscriptionModel

@step("Confirm selected ports have coherent pluggables")
def confirm_ports_have_coherent_pluggables(subscription: SubscriptionModel) -> State:
    fiber_block = subscription.fiber
    terminations = fiber_block.terminations

    for t in terminations:
        port_name = t.port_name
        packet_node = t.host_node

        pluggables = get_name_of_ports_with_coherent_pluggable(packet_node) # this function only expects that the packet_node satisfies the PacketNodeProtocol.

        if port_name not in pluggables:
            raise ValueError(f"Port {port_name} does not have a coherent pluggable")

    return {"subscription": subscription}
```