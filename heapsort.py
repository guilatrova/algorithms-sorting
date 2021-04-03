def heapify(arr, size, root):
    biggest = root
    left = (root * 2) + 1
    right = (root * 2) + 2

    # Handle left child
    left_exists = left < size
    if left_exists and arr[left] > arr[biggest]:
        biggest = left

    # Handle right child
    right_exists = right < size
    if right_exists and arr[right] > arr[biggest]:
        biggest = right

    # Decide whether to swap
    is_root_biggest = biggest == root
    if not is_root_biggest:
        arr[root], arr[biggest] = arr[biggest], arr[root]
        heapify(arr, size, biggest)


def heapsort(arr):
    amt = len(arr)

    # BUILD HEAP:
    # start from middle, decrease until root (index 0)
    for i in range(amt//2 - 1, -1, -1):
        heapify(arr, amt, i)

    # SORT HEAP:
    for i in range(amt-1, 0, -1):
        # Cause randomness
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [26, 25, 9, 59, 37, 16, 68, 24, 34]
    print(f"START ~~> {arr}")

    heapsort(arr)

    print(f"END ~~> {arr}")
