def fibonacci_r(n: int): -> int
    if n<=1:
        return n
    return fibonacci_r(n-1) + fibonacci_r(n-2)
