#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""1. Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
D is a variable whose values should be input to your program in a comma-separated sequence.
"""
import math

c=50
h=30
l = []
for D in d:
    d = input("D: ").split(',')
    square_root = round(math.sqrt(2 * c * int(D) / h))
    l.append(square_root)

print(l)
            


# In[ ]:


"""2. Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default.
"""
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

area_sq = Square(2)
print(area_sq.area())  


# In[17]:


"""3. Create a class to find three elements that sum to zero from a set of n real numbers
Input array: [-25,-10,-7,-3,2,4,8,10]
Expected output: [[-10,2,8],[-7,-3,10]]"""

class example:
    
    def sum_threenum(self, n=[-25, -10, -7, -3, 2, 4, 8, 10]):
        n, sorted_list,i = sorted(n), [], 0
        while i < len(n) - 2:
            j, k = i + 1, len(n) - 1
            while j < k:
                if n[i] + n[j] + n[k] < 0:
                    j += 1
                elif n[i] + n[j] + n[k] > 0:
                    k -= 1
                else:
                    sorted_list.append([n[i], n[j], n[k]])
                    j, k = j + 1, k - 1
                    if j < k and n[j] == n[j - 1]:
                        j += 1
                    elif j < k and n[k] == n[k + 1]:
                        k -= 1
            i += 1
            if i < len(n) - 2 and n[i] == n[i - 1]:
                i += 1
        return sorted_list

print(example().sum_threenum())


# In[ ]:


"""”.
5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
parameter. The constructor must assign the integer value to the age variable after confirming the
argument passed is not negative; if a negative argument is passed then the constructor should set
age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
methods:"""

age = int(input("Enter your Age:"))         

class Person:
   
    def __init__(self,age):
        
        if age <0:
            self.age= 0
            print('Age is not valid, setting age to 0.')
        else:
            self.age=age
    person = Person(age).amIOld()
    def amIOld(self):
        
        if self.age<13:
            print('You are young.')
        elif (self.age>=13 and self.age<=19):
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        self.age+=1    


# In[1]:





# In[ ]:




