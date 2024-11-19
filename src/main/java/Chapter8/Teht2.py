class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
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

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        # Start at Root node
        index = 0
        # Calculate index of possible first child
        child_index = index*2+1
        # While node has at least one child
        while child_index < self._size:
            if child_index+1 < self._size:
                # If two children
                min_index = min(child_index, child_index+1, key=lambda x: self._heap[x])
            else:
                # If only one child
                min_index = child_index
            # Swap values if parent is bigger than child
            if self._heap[index] > self._heap[min_index]:
                self._heap[index], self._heap[min_index] = self._heap[min_index], self._heap[index]   # Swap
                # Update indices
                index = min_index
                child_index = index*2+1
            else:
                # If parent is less than child, then no need to continue.
                return