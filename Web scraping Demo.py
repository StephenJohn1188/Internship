#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[4]:


from bs4 import BeautifulSoup


# In[5]:


import requests


# In[6]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# # Page Content

# In[7]:


soup=BeautifulSoup(page.content)
soup


# In[8]:


first_title=soup.find('div',class_="restnt-info cursor")
first_title


# In[9]:


first_title.text


# # Scraping Loc

# In[10]:


loc=soup.find('div',class_="restnt-loc ellipsis")
loc.text


# # Scraping first price

# In[11]:


sta=soup.find('span',class_="double-line-ellipsis")
sta.text


# In[12]:


sta=soup.find('span',class_="double-line-ellipsis")
sta.text.split()


# In[13]:


sta=soup.find('span',class_="double-line-ellipsis")
sta.text.split()[1]


# # Scraping multiple titles

# In[14]:


title=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    title.append(i.text)
    
title


# # Scraping multiple location

# In[16]:


location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
location


# # Scraping multiple price

# In[17]:


price=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    price.append(i.text)
    
price


# In[18]:


images=[]
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
    
images


# In[20]:


print(len(title),len(location),len(price),len(images))


# In[24]:


import pandas as pd
df=pd.DataFrame({'Titles':title,'Location':location,'Price':price,'Image_Url':images})
df


# In[ ]:





# In[ ]:




