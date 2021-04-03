def heapify(arr, amt, i):
    biggest = i
    left = (i * 2) + 1
    right = (i * 2) + 2

    if left < amt and arr[biggest] < arr[left]:
        biggest = left

    if right < amt and arr[biggest] < arr[right]:
        biggest = right

    if biggest != i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        heapify(arr, amt, biggest)


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
