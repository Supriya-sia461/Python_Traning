#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""1"""
X = range(1,1000) 
Y = xrange (1,1000) 

print ("Range function: ",type(X)) 

print (" xrange function : ",type(Y)) 


"""xrange function is only available in python 3 the main diffrence between them is type , range type is list and xrange type is 'xrange'"""


# In[2]:


"""2"""
"""Tuples are faster than lists."""


# In[5]:


"""3"""
for i in range(1, 1001):
    if((i%3==0) & (i%5==0)):
        print(i)
      


# In[9]:


"""4"""
def example(Input_str):
    vowels = ""
    for i in Input_str:
        if i in "aeiouAEIOU":
            vowels += i
    result = "" 
    for i in Input_str:
        if i in "aeiouAEIOU":
            result += vowels[-1]
            vowels = vowels[:-1]
        else:  
            result += i
    return result  
print(example("Aifgh"))    


# In[ ]:


"""5"""
def printWords(input_string): 
    input_string = input_string.split(' ')
    for word in input_string: 
         if len(word)%2==0:
            print(word)

input_string=input("input your string:")
printWords(input_string) 


# In[ ]:


"""6"""
def pair(x, n, sum):
    count = 0
    for i in range(n-1):
        for j in range(i + 1, n):
            if x[i] + x[j] == sum:
                print("sum of the pair 8 is", (x[i], x[j]))
                count += 1
x=[1,2,3,4,5,6,7,8,9,-1]
n = len(x)
sum = 8
pair(x, n,sum)


# In[ ]:


"""7"""
a=[]
even=[]
odd=[]
n=5
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)


# In[ ]:



"""8"""
string = "12abcbacbaba344ab"
x = []
for i in string:
    if i not in x:
        x.append(i)
for a in x:
    print(a,string.count(a), sep = "=")


# In[ ]:


"""9"""
initail_tuple = (1,2,3,4,5,6,7,8,9,10)
new_tuple = tuple(i for i in initail_tuple if i%2 == 0)
print(new_tuple)


# In[ ]:




