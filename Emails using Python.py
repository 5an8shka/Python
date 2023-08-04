#!/usr/bin/env python
# coding: utf-8

# SENDING EMAILS:

# In[6]:


import smtplib


# In[7]:


smtp_object= smtplib.SMTP('smtp.gmail.com',587)


# In[8]:


smtp_object.ehlo()


# In[9]:


smtp_object.starttls()


# In[10]:


password = input('what is your password: ')


# In[11]:


import getpass


# In[12]:


password=getpass.getpass('Password please: ')


# In[13]:


email=getpass.getpass('Email: ')
password=getpass.getpass('Password: ')
smtp_object.login(email,password)


# In[14]:


from_address=email
to_address=email
subject=input('Enter the subject line: ')
message=input('Enter the message: ')
msg="Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)


# In[15]:


smtp_object.quit()


# In[ ]:





# VIEWING EMAILS:

# In[16]:


import imaplib


# In[18]:


M=imaplib.IMAP4_SSL('imap.gmail.com')


# In[19]:


import getpass


# In[20]:


email=getpass.getpass('Email: ')
password=getpass.getpass('Password: ')


# In[21]:


M.login(email,password)


# In[22]:


M.list()


# In[23]:


M.select('inbox')


# In[24]:


typ,data=M.search(None,'Subject "NEW PYTHON TEST"')


# In[25]:


typ


# In[ ]:





# In[27]:


email_id=data[0]


# In[31]:


result,email_data=M.fetch(email_id,'(RFC822)')        # not running because inbox is empty refer to notebook


# In[33]:


email_data             # not running because inbox is empty refer to notebook


# In[34]:


# for rest refer to notebook


# In[ ]:




