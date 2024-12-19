"""Local Scopes Cannot Use Variables in Other Local Scopes"""

"""def spam():
     eggs = 99
     bacon()
     print(eggs)

def bacon():
     ham = 101
     eggs = 0

spam()"""

"""The Collatz Sequence
Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1."""

"""def collatz(number):
     if(number % 2 == 0):
          return number
     else:
          print( " " , 3*number +1)

collatz(6)"""


"""Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. """

"""height = int(input("Enter the height: "))
base = int(input("Enter the base: "))

Area = 1/2 * base * height

print("The area of triangle is: ",Area)"""


"""Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,"""

"""
print ("Enter the shape of your area--")
print("1. Rectangle ")
print("2. Triangle")

choice = int(input("Enter the choice of shape: "))

if(choice == 1):
    Rect_Len = int(input("Enter the lenght of rectangle: "))
    Rect_width = int(input("Enter the width of rectangle: "))
    Area_of_Rectangle = Rect_Len * Rect_width

    print("The area of rectangle is: ",Area_of_Rectangle)
elif(choice == 2):
    height = int(input("Enter the height: "))
    base = int(input("Enter the base: "))

    Area = 1/2 * base * height

    print("The area of triangle is: ",Area)

else:
    print("Please enter the proper choice...")"""

"""
Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
"""
x = int(input("Enter the number: "))

for i in range(0,x):
    
    for j in range(0,i+1):
        print("* ", end="")
    print()



