#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Task_2 Q1. Write a program in Python to perform the following operation:I
f a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
string."""


x=int(input("Enter your number:"))

if x%3==0 and x%5!=0:
    print("Consultadd")
    
elif x%5==0 and x%3!=0: 
    print("Python Training")
    
while x%5==0 and x%3==0:
    print("Consultadd - Python Training")
    break
    
"""Task_2 Q2. Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average"""

def addition(num1, num2):
    return num1 + num2 



def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2

 
def divide(num1, num2):
    return num1 / num2

def avg(num1, num2,num3,num4):
    return (num1+num2+num3+num4)/4


print("Please select operation -\n" "1. Add\n" "2. Subtract\n" "3. Multiply\n""4. Divide\n") 

select = int(input("Select operations form 1, 2, 3, 4,5 :")) 

num_1 = int(input("Enter first number: ")) 
num_2 = int(input("Enter second number: ")) 

if select == 1:
    print("addition is", addition(num_1, num_2)) 

elif select == 2:
    print("substraction is",subtract(num_1, num_2)) 

elif select == 3:
    print("multiplication is",multiply(num_1, num_2)) 

elif select == 4:
    print("division is",divide(num_1, num_2)) 
    
elif select == 5:
    num_3 = int(input("Enter third number: ")) 
    num_4 = int(input("Enter fourth number: "))
    print("avg is",avg(num_1, num_2,num_3,num_4))
    
else:
    print("Invalid input") 

"""3. Write a program in Python to implement the given flowchart:"""
a=10
b=20
c=30

avg=(a+b+c)/3
print("avg=",avg)

if avg>a and avg>b and avg>c:
    print ("avg is greater than a b c")         
if (avg>a) and (avg>b):
    print ("avg is greater than a b ")
if (avg>a) and (avg>c):
    print ("avg is greater than a c ") 
if (avg>c) and (avg>b):
    print ("avg is greater than b c ")
if (avg>a):
    print ("avg is just greater than a ")
if (avg>b):
    print ("avg is just greater than b ")
if (avg>c):
    print ("avg is just greater than c ")
    
"""4. Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going"""

x=int(input("Enter your number:"))

while True:
    
    if x<0:
        print("It’s Over")
        break
    else:
        print("Good Going")
        break
        
"""5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200.
"""
n=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        n.append(x)
print (n)

"""7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5
"""
for i in range(6):
    if (i == 3 or i==6):
        continue
    print(i)

"""8. Write a program that accepts a string as an input from the user and calculate the number of digits
and letters. 
"""

all_d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 


all_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 


string = input("Input a string: ")

digits = 0
letters = 0


for i in string: 
    if i in all_d: 
        digits += 1


    elif i in all_l: 
         letters += 1

print("Number of digits found in string :", digits) 
print("Number of letters found in string  :", letters) 


"""9a. Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever."""
x=int(input("guess the lucky number:"))

while True:
    if x==5:
        print("Congratulations!!")
        break
    else:

        x=int(input("Please try again:"))



"""9b.Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number)"""

x=int(input("guess the lucky number:"))
if x!=5:
    x=int(input("Please try again:"))

while True:
    if x==5: 
        print("Congratulations!!")
        s = str(input("would like to continue? : "))
    if s in ["no","NO"]:
        print("goodbye")
        break
    else:
        x=int(input("guess the lucky number:"))
        

"""Q10 The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!"""

lucky_num=5
count = 0
while count < 5:
    
    x = int(input("Guess a number:- "))
    
    if x == lucky_num:
        print("Good guess!!","you did in",count, " try")
        
        
    else:
        print("try again!")
    count += 1

print("\nGame over!!")  

"""q11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”"""
lucky_num=5
count = 0
while count < 5:
    
    x = int(input("Guess a number:- "))
    
    if x == lucky_num:
        print("good guess ",count, " try")
        break
        
        
    else:
        print("try again!")
    count += 1

print("\nSorry but that was not very successful”!!")
        

