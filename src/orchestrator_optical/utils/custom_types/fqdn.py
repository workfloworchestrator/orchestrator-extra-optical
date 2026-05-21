# 

from re import match
from typing import Annotated

from pydantic import AfterValidator


def validate_fqdn(value: str) -> str:
    # Regular expression for validating an FQDN
    regex = r"^(?!-)[a-z0-9-]{1,63}(?<!-)(\.[a-z0-9-]{1,63})+$"
    if not match(regex, value):
        raise ValueError(f"'{value}' is not a valid FQDN")
    return value


def validate_fqdn_prefix(value: str) -> str:
    # Regular expression for validating an FQDN
    regex = r"^(?!-)[a-z0-9-]{1,63}(?<!-)(\.[a-z0-9-]{1,63})*$"
    if not match(regex, value):
        raise ValueError(f"'{value}' is not a valid FQDN")
    return value


Fqdn = Annotated[str, AfterValidator(validate_fqdn)]
FqdnPrefix = Annotated[str, AfterValidator(validate_fqdn_prefix)]
