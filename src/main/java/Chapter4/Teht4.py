class Queue():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def enqueue(self, data):
        # Create the new node. Its "next" pointer should point to the current head
        new_node = ListNode(data, prev=None, next=self._head)

        # If the queue is empty, update pointers to the new node
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # If not empty, add the new element at the front
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def dequeue(self):
        # If list is empty, returns None
        if not self._size:
            return None

        # Locate previous_node (the node just before last node)
        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        # If node to remove is first node, then update head pointer
        if node_to_remove == self._head:
            self._head = None
        else:
            # If not, update the pointer of the previous node
            previous_node.next = None   # It is now the last node

        # Update tail pointer
        self._tail = previous_node

        # Update size, remove node and return its content
        self._size -= 1
        value = node_to_remove.data
        del(node_to_remove)
        return value