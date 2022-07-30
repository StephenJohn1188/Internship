#!/usr/bin/env python
# coding: utf-8

# In[48]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[62]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
page


# In[63]:


country=BeautifulSoup(page.content)
country


# # Player Name

# In[102]:


player_name=country.find('td',class_='table-body__cell rankings-table__name name')
player_name


# In[103]:


player_name.text


# In[105]:


player_name=[]
for i in country.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# # Team

# In[96]:


Team=country.find('span',class_='table-body__logo-text')
Team


# In[97]:


Team.text


# In[98]:


Team=[]
for i in country.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# # Rating

# In[89]:


Rating=country.find('td','table-body__cell rating')
Rating


# In[90]:


Rating.text


# In[91]:


Rating=[]
for i in country.find_all('td','table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[94]:


import pandas as pd


# In[108]:


df=pd.DataFrame({"Team": Team, "Rating":Rating})


# In[109]:


df


# In[111]:


df.head(10)


# In[ ]:





# In[ ]:




