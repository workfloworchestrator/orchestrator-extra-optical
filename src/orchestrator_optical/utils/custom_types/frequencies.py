# 

import ast
from typing import Annotated

from pydantic import AfterValidator, BeforeValidator, Field
from typing_extensions import Doc

Frequency = Annotated[
    int,
    Field(ge=191_312_500, le=196_137_500, multiple_of=6_250),
    Doc("A frequency value in MHz."),
]

Bandwidth = Annotated[
    int,
    Field(ge=3125),
    Doc("A bandwidth value in MHz."),
]


def parse_if_string(value):
    if isinstance(value, str):
        return ast.literal_eval(value)
    return value


def validate_passband_order(value: list[Frequency]) -> list[Frequency]:
    if value[0] >= value[1]:
        msg = "Start frequency must be less than end frequency"
        raise ValueError(msg)
    return value


Passband = Annotated[
    tuple[Frequency, Frequency],
    BeforeValidator(parse_if_string),
    AfterValidator(validate_passband_order),
    Doc("A passband, modeled as a tuple of two frequencies."),
]


def disjoint_intervals_overlap_search(
    intervals: list[tuple[int, int]],
    target_interval: tuple[int, int],
) -> tuple[int, int] | None:
    """
    Searches for an overlapping interval in a sorted list of *disjoint* intervals using binary search.
    Intervals include the start and do NOT include the end.

    Args:
        intervals (List[Tuple[int, int]]): A sorted list of disjoint intervals, where each interval is a tuple/list (start, end).
        target_interval (Tuple[int, int]): The interval to search for overlaps with (start, end).

    Returns:
        Optional[Tuple[int, int]]: The interval from `intervals` that overlaps with `target_interval`,
        or None if no such interval exists.
    """
    low = 0
    high = len(intervals) - 1

    while low <= high:
        mid = (low + high) // 2
        current_interval = intervals[mid]

        # Check for overlap:
        if current_interval[0] < target_interval[1] and target_interval[0] < current_interval[1]:
            return current_interval

        if current_interval[0] > target_interval[1]:  # Current interval starts after the target ends
            high = mid - 1
        else:  # current_interval[1] < target_interval[0] Current interval ends before the target starts
            low = mid + 1

    return None


def available_to_used_passbands(
    available_passbands: list[Passband],
    absolute_min_freq: Frequency = 191_325_000,
    absolute_max_freq: Frequency = 196_125_000,
) -> list[Passband]:
    """Calculates used frequency passbands within an absolute frequency range, given a list of available (unused) frequency passbands.

    Args:
        available_passbands: A list of Passbands. Assumed to be
            sorted by start frequency and non-overlapping.
        absolute_min_freq: The minimum frequency of the absolute range.
        absolute_max_freq: The maximum frequency of the absolute range.

    Returns:
        A list of Passband, where each passband represents an used frequency
        passband as (start_freq, end_freq). Returns an empty list if there are no used passbands.
    """
    if absolute_min_freq >= absolute_max_freq:
        msg = "absolute_min_freq must be less than absolute_max_freq"
        raise ValueError(msg)

    # Filter out available bands outside the absolute range and sort them
    valid_available = []
    for start, end in available_passbands:
        if end <= absolute_min_freq or start >= absolute_max_freq:
            continue
        # Constrain available passbands to absolute limits
        valid_available.append((max(start, absolute_min_freq), min(end, absolute_max_freq)))

    # Sort strictly by start frequency
    valid_available.sort(key=lambda x: x[0])

    # Validate that available passbands are disjoint
    for i in range(len(valid_available) - 1):
        if valid_available[i][1] > valid_available[i + 1][0]:
            msg = f"Overlapping available passbands detected: {valid_available[i]} and {valid_available[i+1]}"
            raise ValueError(
                msg
            )

    used_passbands: list[tuple[int, int]] = []
    current_track = absolute_min_freq

    for start, end in valid_available:
        if start > current_track:
            used_passbands.append((current_track, start))
        current_track = max(current_track, end)

    if current_track < absolute_max_freq:
        used_passbands.append((current_track, absolute_max_freq))

    return used_passbands
