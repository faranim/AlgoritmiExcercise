def heap_sort(array):  # Renamed from heapsort to heap_sort
    """
    Sorts the given array using the Heapsort algorithm.

    Parameters:
    - array: The array to be sorted.

    Returns: None. The array is sorted in-place.
    """
    n = len(array)

    # Step 1: Build a max heap
    for start in range((n - 2) // 2, -1, -1):
        sift_down(array, start, n - 1)

    # Step 2: Perform heapsort
    for end in range(n - 1, 0, -1):
        array[0], array[end] = array[end], array[0]  # Swap max to the end
        sift_down(array, 0, end - 1)
