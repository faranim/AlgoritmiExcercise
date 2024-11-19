def fib(n):
    """
    Calculate the Fibonacci's series value for integer n

    Parameters:
    - n: The number to use in the Fibonacci's series.

    Returns: The calculated value of the Fibonacci's series for n
    """
    if n < 2:
        return 1
    prev = prev_prev = 1
    for _ in range(n-1):
        result = prev + prev_prev
        prev, prev_prev = result, prev
    return result