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
