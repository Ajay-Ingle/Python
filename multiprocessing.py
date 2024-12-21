import multiprocessing
import time

"""
the main important thing in multiprocessing is that we can not share the data between the two different process (p1 and p2).

Every process has its own address space(virtual space)

It requires IPC i.e. interprocess communication
"""
def calc_square(numbers):
    for i in numbers:
        time.sleep(10)
        print("Square of the numbers is: ",i*i)
        
def calc_cube(numbers):
    for i in numbers:
        time.sleep(10)
        print("Cube of the numbers is: ",i*i*i)

if __name__ == "__main__" :
  arr=[2,3,8,9]
p1 = multiprocessing.Process(target=calc_square, args=arr,)
p2 = multiprocessing.Process(target=calc_cube, args=arr,)

p1.start()
p2.start()

p1.join()
p2.join()

t = time.time()

print("Done in time: ",time.time()-t)