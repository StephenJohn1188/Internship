#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[3]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[4]:


Books=BeautifulSoup(page.content)
Books


# # Page Title

# In[8]:


Title=Books.find('h2')
Title


# In[9]:


Title.text


# In[10]:


Title=[]
for i in Books.find_all('h2'):
   Title.append(i.text)
Title


# # Author

# In[16]:


Author=Books.find('span',class_="sc-1w3fpd7-0 pgLAT")
Author


# In[17]:


Author.text


# In[18]:


Author=[]
for i in Books.find_all('span',class_="sc-1w3fpd7-0 pgLAT"):
   Author.append(i.text)
Author


# # Published Date

# In[19]:


Date=Books.find('span',class_="sc-1thf9ly-2 bKddwo")
Date


# In[22]:


Date=[]
for i in Books.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
   Date.append(i.text)
Date


# In[23]:


import pandas as pd
df=pd.DataFrame({"Title":Title, "Author":Author, "Published Date":Date})
df


# In[ ]:





# In[ ]:




