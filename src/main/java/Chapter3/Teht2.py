class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = []
        count = 0

        while current_node:
            values.append(current_node.data)
            current_node = current_node.next
            count += 1

        element_label = "element" if count == 1 else "elements"
        return f'<SinglyLinkedList ({count} {element_label}): [{", ".join(values)}]>'


    def append(self, value):
        """
        Append a value to the end of the list.

        Parameters:
        - value: The data to append.

        Returns:
        None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty, point the header to the new node
        if not self._head:
            self._head = node
        else:
            # If list is not empty, find the last element and point it to the new node
            current_node = self._head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        """
        Remove and return the last value from the list.

        Returns:
        - The data of the last node, or None if the list is empty.
        """
        # If the list is empty, return None
        if not self._head:
            return None

        # Find the last node and the one before it
        previous_node = None
        current_node = self._head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next

        # If the node to be deleted is the head, update the head
        if self._head == current_node:
            self._head = None
        else:
            # Otherwise, update the previous node
            previous_node.next = None

        # Finally, remove the node and return its value
        value = current_node.data
        del current_node
        return value
