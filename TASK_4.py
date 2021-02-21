#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""1. Write a program to reverse a string."""

input_string = '“1234abcd' 
output_string=''.join(reversed(input_string)) 
print(output_string) 


# In[110]:



"""2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters."""
input_string=input('Enter your string: ')
l=0
u=0
for i in input_string:
      if(i.islower()):
            l=l+1
      elif(i.isupper()):
            u=u+1
print("lowercase letters are:",l)
print("uppercase letters are:",u)


# In[111]:


""". 3.Create a function that takes a list and returns a new list with unique elements of the first list."""
def unique(l):
  unique_list = []
  for a in l:
    if a not in unique_list:
      unique_list.append(a)
  return unique_list

print(unique([1,1,3,2,5,4,6,7])) 


# In[112]:


"""4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically.
"""
i = str(input("enter your string:"))
i1=i.split("-")
i2=sorted(i1)
i3="-".join(i2)
print("the putput string is:",i3)


# In[113]:


"""5. Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized."""

i = str(input("enter your string:"))

print(i.upper())


# In[114]:


"""6. Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console."""
def sum(s1,s2):
    s=int(s1)+int(s2)
    print("sum is:",s)
sum("1","2")    


# In[44]:


"""7. Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.
"""

def max(s1,s2):
    
    l1=len(s1)
    l2=len(s2)
    if l1>l2:
        print(s1)
    elif l1<l2:
        print(s2)
    else: 
        print(s1)
        print(s2)     
max("abc","pqr")


# In[115]:


"""8. Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included)"""
def Touple():
    l=list()
    for i in range(1,21):
        l.append(i**2)
        print(l)
Touple()    


# In[116]:


"""9. Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers."""  

def showNumbers (limit):
    for i in range(0,limit):
        limit+=1
        if i % 2 != 0: 
            print(i,"odd")
        else:
            print(i,"even")
limit=int(input("Give limit:"))
showNumbers (limit)     


# In[119]:


"""10. Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)"""

l1=range(1,20)
e = lambda x: x % 2 == 0
l2 = list(filter(e, l1))
print(l2)


# In[126]:


"""11. Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10]."""

l1= [1,2,3,4,5,6,7,8,9,10]
square1= list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, l1)))

print(square1)


# In[121]:


"""12. Write a function to compute 5/0 and use try/except to catch the exceptions"""
try:
    x = 5 / 0
except:
    print("Error")


# In[94]:


"""13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce()"""
import functools 
lst=[1,2,3,4,5,6,7]
print(functools.reduce(lambda x1: "".join(str(x),for x in lst))


# In[122]:


"""14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions.
"""

n = range(1, 20)
x=list(filter(lambda x : x % 3 == 0, n))
Y=list(filter(lambda x : x % 7 == 0, n))
print(x,Y)


# In[127]:


"""15. Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation."""

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def square(i):

    return (i * i)

sq_num = map(square, n)

for x in sq_num:

    print(x)


# In[ ]:


"""16. What is the output of the following codes:"""
#1
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
"""Answer: 2"""
#2
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()
"""Answer: 
after f
after f?"""


# In[ ]:




