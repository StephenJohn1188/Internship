#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[27]:


page=requests.get('https://www.cnbc.com/world/?region=world')
page


# In[30]:


news=BeautifulSoup(page.content)
news


# # Headline

# In[32]:


Headline=news.find('div',class_='RiverHeadline-headline RiverHeadline-hasThumbnail')
Headline


# In[34]:


Headline.text


# In[36]:


Headline=[]
for i in news.find_all('div',class_='RiverHeadline-headline RiverHeadline-hasThumbnail'):
   Headline.append(i.text)
Headline


# # Time

# In[49]:


Time=news.find('time')
Time


# In[51]:


Time.text


# In[53]:


Time=[]
for i in news.find_all('time'):
   Time.append(i.text)
Time


# # Newslink

# In[69]:


url = "https://www.cnbc.com/world/?region=world"
webpage = requests.get(url) 
trav = BeautifulSoup(webpage.content, "html.parser")
for link in trav.find_all('a'):
    print(type(link), " ", link)


# In[70]:


trav.text


# In[ ]:





# In[ ]:





# In[ ]:




