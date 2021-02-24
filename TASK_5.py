#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""1. Write a program in Python to allow the error of syntax to be handled using exception handling.
"""
try:
    int('x ++ x')
except:
    print ("Syntax error")


# In[ ]:


"""2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode."""

while (True):

    
        try:
            name = str(input("Please enter name: "))
            print("you have entered:",name)
            f=open('name.txt').read()
            print("this file contains",f)
            
            if (name == f):
                print("name is correct ")
                break
            
                  
            else:raise TypeError
        
    
        except TypeError:
            print(" name is incorrect, please input correct name")
            


# In[ ]:


"""3. Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits” """
while (True):
    try:
        input_range = input("Input your four digit number:")
        input_string = str(input_range) 
        length = len(input_string)
        if (length==4): 
            print("This is correct length")
            break
            
        else: raise ValueError
            
    except ValueError:
        print("Error!The length is too short/long !!! Please provide only four digits")


# In[ ]:


"""4. Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times.
"""
count=0
while count<3:
    try:   
        username=input('Enter username: ')
        password=input('Enter password: ')
        
        if password=='abc' and username=='supriya':
                print('Access granted')
                count=5
                
        elif count<3 and count!=4:
                count+=1
                print("Enter correct username and password:")
                
        else: 
            raise KeyError
            
    except KeyError:
        print("too many attempts")


# In[ ]:


"""6. Read doc.txt file using Python File handling concept and return only the even length string from
the file. Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present"""

myfile = open("myfile.txt", "r")
line = myfile.readlines()
line[2]

