#1. Conditional Statements
#Control the flow based on conditions.
#Syntax:
"""
if condition:
    # Code block for true condition
elif another_condition:
    # Code block for elif
else:
    # Code block for false condition
"""

#2. Loops

#a. for Loop
#Used for iterating over a sequence.
#Syntax:
"""for item in sequence:
    # Code block for each iteration"""

#b. while Loop
#Repeats as long as the condition is true.
#Syntax:
"""while condition:
    # Code block for the loop
"""


#3. Loop Control Statements
#Modify the flow within loops.

#a. break
#Exits the loop immediately.
"""
for item in sequence:
    if condition:
        break

"""
#b. continue
#Skips the current iteration and moves to the next.
"""
for item in sequence:
    if condition:
        continue

"""
#c. pass
#Does nothing; a placeholder.
#Syntax:
"""
for item in sequence:
    pass

"""

#Questions for Practice

"""
1. Conditional Statements
Question: Write a program to check if a given number is:

Positive
Negative
Zero
"""
x = int(input("Enter the number: "))
if(x==0):
    print("The entered number is Zero")

elif(x>0):
    print("The entered number is positive")

else:
    print("The entered number is negative")


"""2. for Loop
Question: Write a program to print all even numbers between 1 and 20."""

for i in range(1,20):
    if (i%2 == 0):
        print(f" {i} is even number")
    i += 1

"""4. break Statement
Question: Write a program that prints numbers from 1 to 10 but stops when it reaches 7."""

print("The break statment ")
for i in range(0,10):
    print(" ",i)
    if(i == 7):
        break
        
    i += 1

"""continue Statement
Question: Write a program that prints numbers from 1 to 10 but skips multiples of 3."""

print("Continue statment program that skips multiple of 3")
for i in range(1,11):
    if(i%3 == 0):
        continue
    else:
        print(" ",i)


"""Ending a Program Early with the sys.exit() Function
The last flow control concept to cover is how to terminate the program. Programs always terminate if the program execution reaches the bottom of the instructions. However, you can cause the program to terminate, or exit, before the last instruction by calling the sys.exit() function. Since this function is in the sys module, you have to import sys before your program can use it."""

import sys

while True:
    print("Type exit to exit")

    response = input()

    if response == "exit":
        sys.exit()
    
    print("you typed " +response+ " .")


# This is a guess the number game.
                                           
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))