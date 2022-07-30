#!/usr/bin/env python
# coding: utf-8

# In[132]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[133]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[134]:


country=BeautifulSoup(page.content)
country


# # Country

# In[135]:


country_name=country.find('span',class_='u-hide-phablet')
country_name


# In[136]:


country_name.text


# In[139]:


country_name=[]
for i in country.find_all('span',class_='u-hide-phablet'):
   country_name.append(i.text)
country_name


# # Matches and Points

# In[148]:


Match=country.find('td',class_='table-body__cell u-center-text')
Match


# In[149]:


Match.text


# In[151]:


Match=[]
for i in country.find_all('td',class_='table-body__cell u-center-text'):
  Match.append(i.text)
Match


# # Rating

# In[152]:


Rating=country.find('td',class_='table-body__cell u-text-right rating')
Rating


# In[153]:


Rating.text


# In[154]:


Rating=[]
for i in country.find_all('td',class_='table-body__cell u-text-right rating'):
  Rating.append(i.text)
Rating


# In[ ]:





# In[ ]:




