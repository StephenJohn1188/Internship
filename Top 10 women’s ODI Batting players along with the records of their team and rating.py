#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[17]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
page


# In[18]:


country=BeautifulSoup(page.content)
country


# # Player Name

# In[36]:


player_name=country.find('td', class_='table-body__cell rankings-table__name name')
player_name


# In[37]:


player_name.text


# In[38]:


player_name=[]
for i in country.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# # Team

# In[39]:


Team=country.find('span',class_='table-body__logo-text')
Team


# In[40]:


Team.text


# In[41]:


Team=[]
for i in country.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# # Rating

# In[42]:


Rating=country.find('td',class_='table-body__cell rating')
Rating


# In[43]:


Rating.text


# In[44]:


Rating=[]
for i in country.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[45]:


import pandas as pd


# In[46]:


df=pd.DataFrame({"Player Name":player_name, "Team": Team, "Rating":Rating})


# In[47]:


df


# In[48]:


df.head(10)


# In[ ]:





# In[ ]:




