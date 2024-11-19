def check_balance(text):
    stack = Stack()
    pairs = 0
    for i, c in enumerate(text):
        if c in '([{':
            stack.push(c)
        elif c in ')]}':
            open_char = stack.pop()
            if open_char and open_char+c in ('()', '[]', '{}'):
                pairs += 1
            else:
                return f"Match error at position {i}"
    if stack.pop() is None:
        return f"Ok - {pairs}"
    else:
        return f"Match error at position {i}"