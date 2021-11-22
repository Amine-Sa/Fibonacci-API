def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def advanced_fibonacci(n, cache):
    if n in [0, 1]:
        return n
    elif cache.get(n):
        return cache.get(n)
    value = advanced_fibonacci(n - 1, cache) + advanced_fibonacci(n - 2, cache)
    cache.set(n, value)
    return value
