#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2 write the syntax of simple if statement
if(condition):
    print()
else:
    print()


# In[8]:


#4 wap to check whether a person is eligible for voting or not?
age=int(input("enter the age"))
if(age>= 18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")


# In[9]:


#5 wap to check whether a num enterred by user is even or not
x=int(input("enter the required number: "))
if(x%2==0):
    print("number is even")
else:
    print("number is odd")


# In[11]:


#6 wap to check whether number is divisible by 7 or not
x=int(input("enter the required number: "))
if(x%7==0):
    print("number is divisible")
else:
    print("number is not divisible")


# In[16]:


#7 wap to display "Hello" if a no. entered by user is a multiple of 5 otherwise print"Bye"
x=int(input("enter the required number: "))
if(x%5==0):
    print("Hello")
else:
    print("Bye")


# In[5]:


#8 wap to calculate the eletricity bill according to following criteria:
#first 100 unit no charge
#next 100units Rs.5/unit
#after 200 units Rs.10/unit
amount=0
x=int(input("enter the required unit: "))
if(x<=100):
    amount=0
if(x>100 and x<=200):
    amount=(x-100)*5
if(x>200):
    amount=500+(x-200)*10
print("Amount to pay: ", amount)    


# In[15]:


#9 wap to display the last digit of a no.
x=int(input("enter the required number: "))
print("The last digit of the given number is: ", x%10)


# In[18]:


#10 wap to check whether the last digit of a number is divisible by 3 or not
x=int(input("enter the required number: "))
if(x%3==0):
    print("number is divisible")
else:
    print("number is not divisible")


# In[ ]:




