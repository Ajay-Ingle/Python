"""
This is basically Map Reduce function
"""

from multiprocessing import Pool

def f(n):
    return n*n

if __name__ == "__main__":
    array = [2,4,6,9]
    p = Pool()
    result = p.map(f,array)
    print(result)
    