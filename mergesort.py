from typing import Iterable

YELLOW = "\033[93m"
ENDC = "\033[0m"


def merge_sort(arr: Iterable):
    if len(arr) == 1:
        return arr

    mid = int(len(arr) / 2)

    left, head_l = arr[:mid], 0
    right, head_r = arr[mid:], 0

    left = merge_sort(left)
    print(f">>> L {left}")
    right = merge_sort(right)
    print(f">>> R {right}")

    merged = []
    while head_l < len(left) and head_r < len(right):
        if left[head_l] < right[head_r]:
            merged.append(left[head_l])
            head_l += 1
        else:
            merged.append(right[head_r])
            head_r += 1

    while head_l < len(left):
        merged.append(left[head_l])
        head_l += 1

    while head_r < len(right):
        merged.append(right[head_r])
        head_r += 1

    print(f"{YELLOW}* {merged}{ENDC}")
    return merged


if __name__ == "__main__":
    arr = [26, 25, 9, 59, 37, 16, 68, 24, 34]
    print(f"START ~~> {arr}")

    arr = merge_sort(arr)

    print(f"END ~~> {arr}")
