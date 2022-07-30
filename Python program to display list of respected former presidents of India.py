#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[5]:


from bs4 import BeautifulSoup
import requests


# In[7]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[9]:


soup=BeautifulSoup(page.content)
soup


# In[20]:


first_title=soup.find_all('h3')
first_title


# In[27]:


Term=soup.find_all('p')
Term


# In[35]:


Detail=soup.find_all('div', class_="presidentListing")
Detail


# In[ ]:





# In[ ]:





# In[30]:


import pandas as pd


# In[32]:


df=pd.DataFrame({"President List": Detail})


# In[33]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[14]:





# In[ ]:




