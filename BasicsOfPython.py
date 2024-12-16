#Data Types
# 1. Numeric: int, float, complex

#int
x = 5
print(x)

#float
x = 7.8
print(x)

#complex
z = 1 + 2j
print(z)

# 2.Text: str
name = "Ajay"
print (name)

# 3.Boolean: bool

is_bulb_on= True

#4.Sequence: list, tuple, range
#5. Mapping: dict
#6.Set: set, frozenset


#2. Input/Output Operations
name = input("Enter the name: ")
#Using f-strings
print(f"So your name is {name}")
#Using .format()
age = 25
print("I am {} years old.".format(age))
#Separator and End Arguments
print("Hello", "World", sep="---", end="!")

#3. Operators

#Arithmetic Operators
#Used for basic mathematical operations.

#+ (Addition)
#- (Subtraction)
#* (Multiplication)
#/ (Division)
#// (Floor Division)
#% (Modulus)
#** (Exponentiation)
a = 10
b = 3
print(a + b)  # 13
print(a / b)  # 3.333
print(a // b)  # 3
print(a ** b)  # 1000

#Comparison Operators
#Used to compare two values.
#== (Equal to)
#!= (Not equal to)
#<, >, <=, >=
x = 5
y = 10
print(x == y)  # False
print(x < y)   # True

#Logical Operators
#Used for combining conditions.
#and, or, not
is_student = True
age = 18
print(is_student and age > 17)  # True


#Bitwise Operators
#Operate on binary numbers.
#& (AND), | (OR), ~ (NOT), ^ (XOR), << (Left Shift), >> (Right Shift)
a = 5  # 0101 in binary
b = 3  # 0011 in binary
print(a & b)  # 1 (0001)
print(a | b)  # 7 (0111)

#Assignment Operators
#Used to assign values to variables.
#=, +=, -=, *=, /=, %=, **=, //=
x = 10
x += 5  # x = x + 5
print(x)  # 15


#Membership Operators
#Check for membership in a sequence.
#in, not in
fruits = ["apple", "banana"]
print("apple" in fruits)  # True
print ("Mango" in fruits) #flase

#Identity Operators
#Check if two variables reference the same object.
#is, is not
x = [1, 2]
y = x
print(x is y)  # True
