"""Pure Pydantic domain mixins for coherent pluggables. No WFO dependencies."""

from pydantic import BaseModel, Field


class CoherentPluggableMixinInactive(BaseModel):
    """Hardware fields for an inactive coherent pluggable."""

    port_name: str | None = Field(default=None, description="The string used to identify the port on the host device.")
    port_description: str | None = Field(default=None, description="Description/Label of the port.")
    fw_version: str | None = Field(default=None, description="Firmware version of the pluggable.")


class CoherentPluggableMixinProvisioning(CoherentPluggableMixinInactive):
    """Hardware fields strictly required during provisioning."""

    port_name: str
    fw_version: str


class CoherentPluggableMixin(CoherentPluggableMixinProvisioning):
    """Hardware fields strictly required when active."""

    port_description: str
