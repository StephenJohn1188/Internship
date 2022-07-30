#!/usr/bin/env python
# coding: utf-8

# In[49]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[57]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
page


# In[58]:


country=BeautifulSoup(page.content)
country


# # Player Name

# In[59]:


player_name=country.find('td', class_='table-body__cell rankings-table__name name')
player_name


# In[60]:


player_name.text


# In[61]:


player_name=[]
for i in country.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# # Team

# In[62]:


Team=country.find('span',class_='table-body__logo-text')
Team


# In[63]:


Team.text


# In[64]:


Team=[]
for i in country.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# # Rating

# In[65]:


Rating=country.find('td',class_='table-body__cell rating')
Rating


# In[66]:


Rating.text


# In[67]:


Rating=[]
for i in country.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[68]:


import pandas as pd


# In[69]:


df=pd.DataFrame({"Player Name":player_name, "Team": Team, "Rating":Rating})


# In[70]:


df


# In[71]:


df.head(10)


# In[ ]:





# In[ ]:




