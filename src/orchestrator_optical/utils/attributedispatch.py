# 

import functools
import types
from collections.abc import Callable
from typing import Any, NoReturn, TypeVar

T = TypeVar("T")


def attributedispatch(*attr_names: str, func: Callable[..., Any] | None = None) -> Any:  # noqa: PLR0915
    """Enables dynamic function dispatching based on one or more attributes' values.

    :param attr_names: One or more attribute names to use for dispatching
    :param func: The function to be decorated (optional)
    :return: A wrapper function with enhanced dispatching capabilities
    """
    if not attr_names:
        msg = "attributedispatch requires at least one attribute name"
        raise TypeError(msg)

    # If the last argument is a callable and func is not set, treat it as the function
    # being decorated (e.g., when called as attributedispatch("attr", my_func))
    if func is None and len(attr_names) > 0 and callable(attr_names[-1]):
        func = attr_names[-1]
        attr_names = attr_names[:-1]

    # If no implementation is passed, return a decorator
    if func is None:
        return lambda f: attributedispatch(*attr_names, func=f)

    # Validate that we have at least one attribute name remaining
    if not attr_names:
        msg = "attributedispatch requires at least one attribute name"
        raise TypeError(msg)

    # Create registries to manage different function implementations
    registry: dict[Any, Callable[..., Any]] = {}

    def dispatch(obj: Any) -> Callable[..., Any]:
        """Core dispatching logic to find the appropriate implementation.

        :param obj: The object being dispatched
        :return: The most appropriate implementation function
        :raises AttributeError: If any of the specified attributes do not exist
        """
        # Verify that the object has all specified attributes
        missing_attrs = [name for name in attr_names if not hasattr(obj, name)]
        if missing_attrs:
            msg = f"Object {obj!r} does not have attribute(s): {', '.join(repr(name) for name in missing_attrs)}"
            raise AttributeError(msg)

        # Extract the value of the specified attribute(s)
        if len(attr_names) == 1:
            attr_value = getattr(obj, attr_names[0])
        else:
            attr_value = tuple(getattr(obj, name) for name in attr_names)

        # Look for an exact match of the attribute value in our registry
        if attr_value in registry:
            return registry[attr_value]

        # If no specific implementation is found, fall back to the default implementation
        return func

    def register(*attr_values: Any, implementation: Callable[..., Any] | None = None) -> Any:
        """Register a specific implementation for a given attribute value or value combination.

        :param attr_values: The attribute value(s) to match
        :param implementation: The function to use for this attribute value(s)
        :return: Decorator or registered function
        """
        # If no implementation is provided, check if the last value is the callable
        if implementation is None:
            if attr_values and callable(attr_values[-1]):
                implementation = attr_values[-1]
                attr_values = attr_values[:-1]
            else:
                return lambda f: register(*attr_values, implementation=f)

        # Determine registry key format:
        # If dispatching on a single attribute, keep the key as a single value for backwards compatibility.
        # If dispatching on multiple attributes, use a tuple of values.
        if len(attr_names) == 1 and len(attr_values) == 1:
            key = attr_values[0]
        elif len(attr_names) > 1 and len(attr_values) == 1 and isinstance(attr_values[0], tuple):
            # Support register((val1, val2)) in addition to register(val1, val2)
            key = attr_values[0]
        else:
            key = attr_values

        # Store the implementation in the registry
        registry[key] = implementation
        return implementation

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """The main wrapper function that orchestrates the dispatching.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the dispatched function
        :raises TypeError: If no arguments are provided
        """
        # Ensure at least one argument is passed
        if not args:
            msg = f"{func.__name__} requires at least 1 positional argument"
            raise TypeError(msg)

        # Guard only the dispatch resolution lookup
        try:
            target_func = dispatch(args[0])
        except Exception as e:
            display_names = attr_names[0] if len(attr_names) == 1 else attr_names
            msg = (
                f"Dispatch lookup failed for {func.__name__} on attribute(s) {display_names!r}. "
                f"Error: {e}"
            )
            raise TypeError(
                msg
            ) from e

        # Execute the resolved target function directly to preserve its traceback
        return target_func(*args, **kwargs)

    wrapper.register = register
    wrapper.dispatch = dispatch
    wrapper.registry = types.MappingProxyType(registry)

    return wrapper


def attribute_dispatch_base(func: Callable, attr_name: str | tuple[str, ...] | list[str], attr_value: Any) -> NoReturn:
    """Raise a TypeError with information about supported attribute values.

    Args:
        func: The function being dispatched
        attr_name: Name of the attribute(s) being dispatched on
        attr_value: The unsupported attribute value(s) that was encountered

    Raises:
        TypeError: Always, with details about supported values
    """
    registry = func.registry
    supported_values = ", ".join(str(k) for k in registry)
    msg = (
        f"`{func.__name__}` called for unsupported value '{attr_value}' for attribute '{attr_name}'. "
        f"Supported values are: {supported_values}"
    )
    raise TypeError(msg)