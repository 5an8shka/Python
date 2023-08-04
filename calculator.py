#!/usr/bin/env python
# coding: utf-8

# In[7]:


a=int(input("enter the first number:"))
b=int(input("enter the second number"))
def add():
    s=a+b
    print("The sum is:",s)
def sub():
    diff=a-b
    print("the difference is:",diff)
def mul():
    pro=a*b
    print("the product is:",pro)
def div():
    quo=a/b
    print("the quotient is:",quo)
def rem():
    re=a%b
    print("the remainder is:",re)
def choice():
    user=input("Enter the full name of the function you want to perform:")
    if user=='addition':
        add()
    elif user=='subtraction':
        sub()
    elif user=='multiplication':
        mul()
    elif user=='division':
        div()
    elif user=='remainder':
        rem()
    else:
        print("The function entered is not defined")
choice()


# In[ ]:




