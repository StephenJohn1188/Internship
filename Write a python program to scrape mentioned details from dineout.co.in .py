#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[33]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/welcome-back')
page


# In[34]:


soup=BeautifulSoup(page.content)
soup


# # Restaurant Name

# In[35]:


RN=soup.find('div',class_="restnt-info cursor")
RN


# In[36]:


RN.text


# In[38]:


RN=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    RN.append(i.text)
    
RN


# # Cusines

# In[51]:


price=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    price.append(i.text)
    
price


# # Location

# In[55]:


location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
location


# # Images

# In[57]:


images=[]
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
    
images


# # Rating

# In[77]:


RT=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    RT.append(i.text)
    
RT


# In[71]:


import pandas as pd


# In[79]:


df=pd.DataFrame({"Restaurant Name":RN, "Cusines":price, "Location":location, "Ratings":RT,"Images_Url":images})


# In[80]:


df


# In[ ]:




