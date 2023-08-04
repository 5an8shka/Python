#!/usr/bin/env python
# coding: utf-8

# DISPLAYING INFORMATION:
# 

# In[1]:


print([1,2,3])


# In[2]:


print([1,2,3])
print([4,5,6])
print([7,8,9])


# In[3]:


def display (r1,r2,r3):
    print(r1)
    print(r2)
    print(r3)


# In[4]:


example_row=([1,2,3])
display(example_row,example_row,example_row)


# In[5]:


row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']


# In[6]:


display(row1,row2,row3)


# In[7]:


row2[1]='X'


# In[8]:


display(row1,row2,row3)


# ACCEPTING USER INPUT:

# In[10]:


input('please enter a value : ')


# In[11]:


result=input('please enter a value : ')


# In[12]:


result


# In[13]:


type(result)    #input function is always going to return a string


# In[16]:


result_int=int(result)


# In[17]:


type(result_int)


# In[18]:


position_index=int(input('choose an input position: '))


# In[21]:


type(position_index)


# In[22]:


row1[position_index]


# In[ ]:


result=input('enter a number: ')


# In[ ]:


2+2   


# In[1]:


# It happened because python is still waiting for the user interaction from the input. So only when the value 
    # is entered in the input box the rest of the cells will execute.
# Also if we try to run the cell twice, the input box will disappear and the upcoming cells will also not execute since
    # it is still waiting for the first execution to give the input.


# VALIDATING USER INPUT:

# In[1]:


position_index=int(input('choose an input position: '))


# In order to avoid such errors we validate user input using while loop to ask the user for the correct input 

# In[2]:


def user_choice():
    choice=input('Please enter a number (0-10) : ')
    return int(choice)


# In[3]:


user_choice()


# In[4]:


user_choice()


# In[7]:


def user_choice():
    choice='wrong'
    while choice.isdigit()==False:
        
        choice=input('Please enter a number (0-10) : ')
        if choice.isdigit()==False:
            print('Sorry that is not a digit!')
    return int(choice)


# In[8]:


user_choice()


# In[9]:


result='wrong value'


# In[10]:


acceptable_value=[0,1,2]


# In[11]:


result in acceptable_value


# In[12]:


result not in acceptable_value


# In[15]:


def user_choice():
    
    #VARIABLES
    
    #initial
    choice='wrong'
    acceptable_range=range(0,10)
    within_range=False
    
    #TWO CONDITIONS TO CHECK
    #DIGIT OR WITHIN_RANGE==False
    while choice.isdigit()==False or within_range==False:
        
        choice=input('Please enter a number (0-10) : ')
        
        #DIGIT CHECK
        if choice.isdigit()==False:
            print('Sorry that is not a digit!')
        
        #RANGE CHECK
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                within_range=True
            else:
                print('Sorry you are out of acceptable range')
                within_range=False
                
    return int(choice)


# In[16]:


user_choice()


# SIMPLE USER INTERACTION:

# In[17]:


game_list=[0,1,2]


# In[19]:


def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)


# In[21]:


display_game(game_list)


# In[25]:


def position_choice():
    choice='wrong'
    
    while choice not in ['0','1','2']:
        choice=input('Pick a position (0,1,2): ')
        if choice not in ['0','1','2']:
            print ('Sorry invalid choice!!')
            
    return int(choice)
    


# In[26]:


position_choice()


# In[33]:


def replacement_choice(game_list,position):
    user_placement=input('Type a string to place at position: ')
    game_list[position]=user_placement
    return game_list


# In[34]:


replacement_value(game_list,1)


# In[35]:


def gameon_choice():
    
    choice='wrong'
    
    while choice not in ['Y','N']:
        choice=input('Keep playing (Y or N): ')
        if choice not in ['Y','N']:
            print ('Sorry I dont understand, please choose Y or N: ')
    if choice=='Y':
        return True
    else:
        return False


# In[36]:


gameon_choice()


# In[38]:


game_on=True
game_list=[0,1,2]

while game_on:
    display_game(game_list)
    position= position_choice()
    game_list=replacement_choice(game_list,position)
    display_game(game_list)
    game_on=gameon_choice()


# In[ ]:




