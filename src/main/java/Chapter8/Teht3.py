def binary_search_iterative(array, value):
    """
    Performs a binary search in the the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    # Prepare variables
    start = 0
    end = len(array) - 1
    # Loop while pointer do not cross
    while start <= end:
        # Calculate the midpoint
        midpoint = start + (end - start + 1) // 2
        # If the wanted value is in the midpoint, return its index
        if array[midpoint] == value:
            return midpoint
        # If not, update the start or end pointers acordingly
        if value < array[midpoint]:
            end = midpoint - 1
        if value > array[midpoint]:
            start = midpoint + 1
    # If not found until now, return None
    return None