#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1. Create three variables in a single line and assign values to them in such a manner that each one ofthem belongs to a different data type.

a, b, c = 1, 2.01, 'string'

print(a) #int
print(b) #float
print(c) #string


# In[11]:


# 2. Create a variable of type complex and swap it with another variable of type integer

i=(1+0j)
a=10

print( "The vaue of i before swap:", i)

i=a

print ("The new value of i:",i)


# In[16]:


#Q3 a: Swap two numbers using a third variable and do the same task without using any third variable.
x=1
y=2

t = x
x = y
y = t

print("x:",x)
print("y:",y)

print ("---------------------------------------")

#Q3 b: Swap two numbers using a third variable and do the same task without using any third variable.

x=1
y=2

x, y = y, x

print("x1:",x)
print("y1:",y)


# In[20]:


""""Q4 Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output."""

a = input("Enter your value of a from 1 to 10: ") 
print(a)

b = input("Enter your value of b from 1 to 10: ") 
print(b)

z= int(a)+ int(b)

z=z+30

print("z is:",z)


# In[21]:


#6. Write a program to check the data type of the entered values.

i = 1
print(type(i))

j = 1.20
print(type(j))

k = 'abc'
print(type(k))


# In[24]:


#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE

Upper='ABC'
lower='abc'
snake='abc'

print(Upper, lower, snake)


# In[29]:


#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’again. Will it change the value? If Yes then Why?

a=10 
print("old value of a:",a)

a="abc"
print("updated value of a:",a)

""" Answer: yes the value of variable a changed according to new data type the reson is python updates the old avlue and replace it with the new one, kind of by overriding it by new type"""


# In[ ]:




