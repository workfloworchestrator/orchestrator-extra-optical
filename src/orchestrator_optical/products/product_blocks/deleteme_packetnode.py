from typing import Annotated

from annotated_types import Len
from orchestrator.domain.base import ProductBlock

from orchestrator_optical.products.product_blocks.deleteme_location import ReplaceMeLocation
from orchestrator_optical.utils.custom_types.fqdn import Fqdn
from orchestrator_optical.utils.custom_types.ip_address import IPAddress

IpAddressesList = Annotated[
    list[IPAddress], Len(min_length=1, max_length=10), "List of the management IP addresses of the device."
]


class ReplaceMePacketNode(ProductBlock, product_block_name="ReplaceMePacketNode"):
    location: ReplaceMeLocation
    sw_version: str
    vendor_platform: str
    fqdn: Fqdn
    management_ips: IpAddressesList
