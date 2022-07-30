#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[3]:


page=requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page


# In[5]:


book=BeautifulSoup(page.content)
book


# # Rank

# In[9]:


Rank=book.find('td',class_='gsc_mvt_p')
Rank


# In[11]:


Rank.Text


# In[12]:


Rank=[]
for i in book.find_all('td',class_='gsc_mvt_p'):
   Rank.append(i.text)
Rank


# # Publications

# In[14]:


Pub=book.find('td',class_='gsc_mvt_t')
Pub


# In[15]:


Pub.text


# In[16]:


Pub=[]
for i in book.find_all('td',class_='gsc_mvt_t'):
   Pub.append(i.text)
Pub


# # H5: Index

# In[31]:


H5=book.find('a',class_='gs_ibl gsc_mp_anchor')
H5


# In[32]:


H5.text


# In[35]:


H5=[]
for i in book.find_all('a',class_='gs_ibl gsc_mp_anchor'):
   H5.append(i.text)
H5


# # H5: Median

# In[37]:


h5=book.find('span',class_='gs_ibl gsc_mp_anchor')
h5


# In[38]:


h5.text


# In[39]:


h5=[]
for i in book.find_all('span',class_='gs_ibl gsc_mp_anchor'):
   h5.append(i.text)
h5


# In[40]:


import pandas as pd


# In[41]:


df=pd.DataFrame({"Rank":Rank,"Publication":Pub,"H5 Ixdex":H5,"H5 Median":h5})


# In[42]:


df


# In[ ]:




