import multiprocessing

def calc_square(numbers, result):
    for idx,i in enumerate(numbers):
        print("Square of the numbers is: ",i*i)
        result[idx] = i*i

if __name__ == "__main__":
    array = [2,3,4,9]
    
    """sharedMemoryVariable"""
    result = multiprocessing.Array('i',4)

    p = multiprocessing.Process(target=calc_square, args=(array, result) )

    p.start()
    p.join()

    print("Shared memory: ",result[:])