#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""1. Create a list of 10 elements of four different data types like int, string, complex and float."""
l=[1,"abc",1+0j,1.2,"pqr",1,2+0j,1.3,"TASK3",23]
print(l)


# In[2]:


"""2. Create a list of size 5 and execute the slicing structure"""

l=[1,"abc",1+0j,1.2,"pqr"]
print(l[::2])
print(l[2::])
print(l[1:4])


# In[3]:


"""3. Write a program to get the sum and multiply of all the items in a given list."""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1 = 0
l2 = 1
for i in l:
    l1 += i
for i in l:
    l2 *= i
print("Sum :", l1)
print("Multiplication:", l2)


# In[4]:


"""4. Find the largest and smallest number from a given list"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("max is",max(l))
print("min is",min(l))


# In[5]:


"""5. Create a new list which contains the specified numbers after removing the even numbers from a
predefined list."""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l=[x for x in l if x%2!=0]
print("odd numbers are:",l)


# In[6]:


"""6. Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included)."""
def num_sq():
    square = list()
    for i in range(1,30):
        square.append(i**2)
    print(square[:5]) #first five 
    print(square[-5:]) #last five
num_sq()


# In[7]:


"""7. Write a program to replace the last element in a list with another list.
"""
l1=[1,3,5,7,9,10] 
l2=[2,4,6,8]
l_new=l1.pop(5) #removing elelment by using index
print(l1)
l1.extend(l2)
print(l1)


# In[8]:


"""8 Create a new dictionary by concatenating the following two dictionaries:"""

def merge(a, b):
    return(b.update(a))

a= {1:10,2:20} 
b= {3:30,4:40}


print(merge(a, b))

print(b)


# In[ ]:


"""9 Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).
"""
i=int(input("input n: "))
d = dict()

for x in range(1,i+1):
    d[x]=x*x

print(d) 


# In[ ]:


"""10 Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
"""
l=input("Enter numbers separated by a comma:").split(',')
t=tuple(l)
print ("The list is: ", l)
print("\n" ,"The tuple is:",t)


# In[ ]:




