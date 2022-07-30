#!/usr/bin/env python
# coding: utf-8

# In[37]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[38]:


from bs4 import BeautifulSoup
import requests


# In[39]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[40]:


soup=BeautifulSoup(page.content)
soup


# In[50]:


first_title=soup.find('h3')
first_title


# In[51]:


first_title.text


# In[52]:


first_title=[]
for i in soup.find_all('h3'):
    first_title.append(i.text)
first_title


# In[53]:


Term=soup.find('p')
Term


# In[54]:


Term.text


# In[55]:


Term=[]
for i in soup.find_all('p'):
    Term.append(i.text)
Term


# In[59]:


Detail=soup.find('div', class_="presidentListing")
Detail


# In[60]:


Detail.text


# In[65]:


Detail=[]
for i in soup.find_all('div', class_="presidentListing"):
    Detail.append(i.text)
Detail


# In[66]:


import pandas as pd
df=pd.DataFrame({"PresidentiaL List":Detail})
df


# In[ ]:




