# Iterators An iterator is an object that implements the __iter__() and __next__() methods. It allows traversing through elements of a container (like lists or tuples).

myList = [1,2,3,4,5]
iterator = iter(myList)

print(next(iterator))
print(next(iterator))
print(next(iterator))