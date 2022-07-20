def fibonacci_at(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_at(n - 1) + fibonacci_at(n - 2)
