#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension.
"""
input_string = input("input your string:")
  
upper = [char for char in input_string if char.isupper()] 
   
print(" string which is uppercase : " , upper) 


# In[2]:


"""2. Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
"""
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
output = dict(zip(students, subjects)) 
print(output)


# In[ ]:


"""4. Write a program in Python using generators to reverse the string."""
input_string = input("input your string:")
def reverse(input_string):
    length_str = len(input_string)
    for i in range(length_str - 1, -1, -1):
        yield input_string[i]

for string in rev_str(input_string):
    print(string)


# In[ ]:


"""5. Write an example on decorators."""
def decorator_fun(func2): 
    def fun1():
        
        print("Initial execution") 
        func2()
        print("After execution") 
    return fun1
def fun3(): 
    print("we are inside the function")
fun3 = decorator_fun(fun3)
fun3() 
        

