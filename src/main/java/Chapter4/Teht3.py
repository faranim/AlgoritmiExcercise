class StackBasedQueue():
    def __init__(self):
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        self._size = 0

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        # Push the data to the Inbound Stack
        self._InboundStack.push(data)
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            return None

        if len(self._OutboundStack) == 0:
            # If Outbound Stack is empty, transfer whatever is in the Inbound Stack
            while data := self._InboundStack.pop():
                self._OutboundStack.push(data)

        # Return the pop of Outbound Stack
        self._size -= 1
        return self._OutboundStack.pop()