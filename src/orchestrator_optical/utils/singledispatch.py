# 


from collections.abc import Callable
from itertools import filterfalse
from typing import Any, NoReturn


def single_dispatch_base(func: Callable, value: Any) -> NoReturn:
    registry = func.registry  # type: ignore

    supported_models = ", ".join(map(str, filterfalse(lambda t: t is object, registry.keys())))
    model_type = type(value)
    raise TypeError(
        f"`{func.__name__}` called for unsupported model type {model_type}. "
        f"Supported model types are: {supported_models}"
    )
