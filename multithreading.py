"""
for a given list of numbers calculate the square and cube of the numbers
"""

import time
import threading

def calc_square(numbers):
    for i in numbers:
        time.sleep(0.2)
        print("Square: ", i*i)

def calc_cube(numbers):
    for i in numbers:
        time.sleep(0.2)
        print("Cube: ", i*i*i)

arr = [2,3,8,9]

t = time.time()
print("The time in sec since this epoch: ",t)

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in time: ",time.time()-t)