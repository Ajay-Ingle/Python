# Generators A generator is a function that yields values one at a time, rather than returning them all at once. It is defined using the yield keyword.

# A generator to produce the first n Fibonacci numbers.

def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a + b

for num in fibonacci(5):
    print(num)


# Benefits of Generators:

# Efficient memory usage, as values are generated lazily (one at a time).
# Useful for iterating over large datasets.