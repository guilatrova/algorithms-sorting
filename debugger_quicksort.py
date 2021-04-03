import os
from typing import Iterable


PRINT_PREFIX = "*"
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
STEP_DEBUG = os.getenv("STEP_DEBUG", "true").lower() == "true"
CHANGED = "\033[93m"
UNCHANGED = "\033[91m"
PIVOT = "\033[92m"
ENDC = "\033[0m"


class DebugMixin:
    def on_swap(self, p1: int, p2: int):
        if not DEBUG:
            return

        print(f"{PRINT_PREFIX * 9} [", end="")
        for idx, n in enumerate(self.arr):
            sufix = ", " if idx < len(self.arr) - 1 else ""

            if idx == self.pivot:
                print(f"{PIVOT}{n}{ENDC}{sufix}", end="")
            elif idx in (p1, p2):
                color = CHANGED if p1 != p2 else UNCHANGED
                print(f"{color}{n}{ENDC}{sufix}", end="")
            else:
                print(f"{n}{sufix}", end="")

        print("]")

        if STEP_DEBUG:
            input()


class QuickSortAlgorithm(DebugMixin):
    def __init__(self, arr: Iterable[int]):
        self.arr = arr

    def swap(self, p1: int, p2: int):
        tmp = self.arr[p2]
        self.arr[p2] = self.arr[p1]
        self.arr[p1] = tmp
        self.on_swap(p1, p2)

    def _on_start(self):
        print(f"START ~~> {self.arr}")

    def _on_end(self):
        print(f"END   ~~> {self.arr}")

    def quicksort(self):
        self._on_start()
        self._quicksort(0, len(self.arr) - 1, PRINT_PREFIX)
        self._on_end()

    def _quicksort(self, start: int, end: int, pprefix: str):
        if start >= end:
            return

        pivot = self.arr[start]
        self.pivot = start
        pos = end

        for idx in range(end, start, -1):
            if self.arr[idx] > pivot:
                self.swap(idx, pos)
                pos -= 1

        self.swap(start, pos)

        self._quicksort(start, pos - 1, PRINT_PREFIX + pprefix)
        self._quicksort(pos + 1, end, PRINT_PREFIX + pprefix)


if __name__ == "__main__":
    arr = [26, 25, 9, 59, 37, 16, 68, 24, 34]

    algo = QuickSortAlgorithm(arr)
    algo.quicksort()
