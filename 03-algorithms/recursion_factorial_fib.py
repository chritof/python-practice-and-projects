from functools import lru_cache

def factorial(n: int) -> int:
    """Return n! (n factorial)."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Return the nth Fibonacci number using memoization."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print("5! =", factorial(5))     # 120
    print("fib(10) =", fib(10))     # 55
