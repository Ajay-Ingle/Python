"""
for a given list of numbers calculate the square and cube of the numbers
"""

import time

def calc_square(numbers):
    for i in numbers:
        print("Square of the numbers")
        time.sleep(0.2)
        print("Square: ", i*i)

def calc_cube(numbers):
    for i in numbers:
        print("Cube of the numbers")
        time.sleep(0.2)
        print("Cube: ", i*i)

arr = [2,3,8,9]
calc_square(arr)
calc_cube(arr)
t = time.time()
print("The time in sec since this epoch: ",t)
print("Done in time: ",time.time()-t)