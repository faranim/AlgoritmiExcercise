class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        # Start at the end of the heap
        index = self._size - 1
        # Calculate index of parent element
        parent_index = (index-1) // 2
        # While not at Root node and value less than its parent
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swap value with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Update indices
            index = parent_index
            parent_index = (index-1) // 2