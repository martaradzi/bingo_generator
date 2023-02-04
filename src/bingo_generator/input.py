import math
from pathlib import Path
from typing import Collection, List


def read_file(path: Path) -> Collection[str]:
    """Read it in the input file."""
    input_list: List[str] = []
    with open(path, "r") as f:
        for line in f:
            input_list.append(line.strip().lower())

    test_input(input_list)

    return input_list


def test_input(input_data: Collection[str]) -> None:
    """Test if input file is correct"""
    n = len(set(input_data))

    if len(input_data) != n:
        raise ValueError("Duplicated values in the input array.")

    print(f"Found {n} unique inputs")
    root = math.isqrt(n)
    if root * root != n:
        raise ValueError(
            "The number of input strs cannot be made into a bingo board. "
            "The number of inputs must be a perfect square root."
        )
