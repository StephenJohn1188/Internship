#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[7]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[9]:


country=BeautifulSoup(page.content)
country


# # Country

# In[13]:


country_name=country.find('span',class_='u-hide-phablet')
country_name


# In[14]:


country_name.text


# In[16]:


country_name=[]
for i in country.find_all('span',class_='u-hide-phablet'):
    country_name.append(i.text)
country_name


# In[17]:


match_no=country.find('td',class_='table-body__cell u-center-text')
match_no


# In[18]:


match_no.text


# # Matches and Points

# In[39]:


match_no=[]
for i in country.find_all('td',class_='table-body__cell u-center-text'):
    match_no.append(i.text)
match_no


# # Ratings

# In[23]:


rating_no=country.find('td',class_='table-body__cell u-text-right rating')
rating_no


# In[25]:


rating_no.text


# In[26]:


rating_no=[]
for i in country.find_all('td',class_='table-body__cell u-text-right rating'):
    rating_no.append(i.text)
rating_no

