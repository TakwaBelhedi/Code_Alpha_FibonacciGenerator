from functools import wraps
import sys
def memorize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]
    return wrapper
@memorize
def fibonacci(n: int):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n-2)

if __name__ == '__main__':
    sys.setrecursionlimit(10_000)
    f = fibonacci(3000)
    print(f)
