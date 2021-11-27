from functools import cache
from math import *


def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def functools_fibonacci(n):
    if n in [0, 1]:
        return n
    return functools_fibonacci(n - 1) + functools_fibonacci(n - 2)


def advanced_fibonacci(n, cache):
    if n in [0, 1]:
        return n
    elif cache.get(n):
        return cache.get(n)
    value = advanced_fibonacci(n - 1, cache) + advanced_fibonacci(n - 2, cache)
    cache.set(n, value)
    return value


def reverse_fibonacci(k):
    if k == 0:
        return 0
    return ceil(log(k * sqrt(5) + 1 / 2) / log((1 + sqrt(5)) / 2))
