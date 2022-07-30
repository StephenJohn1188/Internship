#!/usr/bin/env python
# coding: utf-8

# In[115]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[117]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
page


# In[118]:


country=BeautifulSoup(page.content)
country


# # Player Name

# In[119]:


player_name=country.find('td',class_='table-body__cell rankings-table__name name')
player_name


# In[120]:


player_name.text


# In[121]:


player_name=[]
for i in country.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# # Team

# In[122]:


Team=country.find('span',class_='table-body__logo-text')
Team


# In[123]:


Team.text


# In[124]:


Team=[]
for i in country.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# # Rating

# In[125]:


Rating=country.find('td',class_='table-body__cell rating')
Rating


# In[126]:


Rating.text


# In[127]:


Rating=[]
for i in country.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[128]:


import pandas as pd


# In[129]:


df=pd.DataFrame({"Player Name":player_name, "Team": Team, "Rating":Rating})


# In[130]:


df


# In[131]:


df.head(10)


# In[ ]:





# In[ ]:




