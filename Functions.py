"""Local Scopes Cannot Use Variables in Other Local Scopes"""

def spam():
     eggs = 99
     bacon()
     print(eggs)

def bacon():
     ham = 101
     eggs = 0

spam()

"""The Collatz Sequence
Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1."""

def collatz(number):
     if(number % 2 == 0):
          return number
     else:
          print( " " , 3*number +1)

collatz(6)