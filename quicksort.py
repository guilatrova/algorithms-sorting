import os
from typing import Iterable


PRINT_PREFIX = "*"
DEBUG = os.getenv("DEBUG", "true").lower() == "true"


def swap(arr: Iterable, p1: int, p2: int):
    tmp = arr[p2]
    arr[p2] = arr[p1]
    arr[p1] = tmp


def quicksort(arr: Iterable, start: int, end: int, pprefix: str = PRINT_PREFIX):
    if start >= end:
        return

    pivot = arr[start]
    pos = end

    for idx in range(end, start, -1):
        if arr[idx] > pivot:
            swap(arr, idx, pos)
            pos -= 1

    swap(arr, start, pos)

    if DEBUG:
        print(f"{pprefix} {arr}")

    quicksort(arr, start, pos - 1, PRINT_PREFIX + pprefix)
    quicksort(arr, pos + 1, end, PRINT_PREFIX + pprefix)


if __name__ == "__main__":
    arr = [26, 25, 9, 59, 37, 16, 68, 24, 34]
    print(f"START ~~> {arr}")

    quicksort(arr, 0, len(arr) - 1)

    print(f"END ~~> {arr}")
