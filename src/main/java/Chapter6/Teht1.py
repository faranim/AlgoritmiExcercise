class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'

class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0

    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        return len(key) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.

        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        # Start to search from the given position
        current = start

        # While that position is in use, enter the loop
        while self.slots[current]:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size

            # If we reach again the given position, that means
            # a whole cycle has been completed and there was no free
            # positions available
            if current == start:
                return None

        # After the loop, current points to a free position
        return current