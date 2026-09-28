def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

def iterative_factorial(n):
    answer = 1
    while n != 0 and n != 1:
        answer *= n
        n -= 1
    
    return answer

def recursive_fibonacci(n):
    if n < 2:
        return n
    
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def iterative_fibonacci(n):
    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b
    return a

def improved_recursive_fibonacci(n):
    cache = {}

    def _improved_recursive_fibonacci(n):
        if n in cache:
            return cache[n]

        if n < 2:
            return n

        cache[n] = _improved_recursive_fibonacci(n - 1) + _improved_recursive_fibonacci(n - 2)
        return cache[n]

    return _improved_recursive_fibonacci(n)
