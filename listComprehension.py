# [expression for item in iterable if condition]
# Create a list of squares of even numbers between 1 and 10.

square = [item**2 for item in range(1,11) if item%2 == 0]
print(square)

# Advantages:

# More readable and concise than loops.
# Often faster than equivalent for-loop constructions.