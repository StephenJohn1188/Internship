#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


import requests


# In[4]:


topics=requests.get("https://www.imdb.com/search/title/?groups=top_100")


# In[6]:


content=topics.text


# In[8]:


content[:500]


# In[10]:


from bs4 import BeautifulSoup


# In[11]:


doc = BeautifulSoup(topics.text,'html.parser')


# In[13]:


doc.find('title')


# In[20]:


def get_movie_titles(doc):
    
    selection_class="lister-item-header"
    movie_title_tags=doc.find_all('h3',{'class':selection_class})
    movie_titles=[]

    for tag in movie_title_tags:
        title = tag.find('a').text
        movie_titles.append(title)
        
        
    return movie_titles


# In[21]:


titles = get_movie_titles(doc)


# In[52]:


titles[:100]


# In[54]:


def get_movie_rating(doc):
    rating_selector="inline-block ratings-imdb-rating"            
    movie_rating_tags=doc.find_all('div',{'class':rating_selector})
    movie_rating_tagss=[]
    for tag in movie_rating_tags:
        movie_rating_tagss.append(tag.get_text().strip())
    return movie_rating_tagss


# In[74]:


ratings = get_movie_rating(doc)
ratings[:5]


# In[56]:


def get_movie_year(doc):
    year_selector = "lister-item-year text-muted unbold"           
    movie_year_tags=doc.find_all('span',{'class':year_selector})
    movie_year_tagss=[]
    for tag in movie_year_tags:
        movie_year_tagss.append(tag.get_text().strip()[1:5])
    return movie_year_tagss


# In[76]:


years = get_movie_year(doc)
years[:5]


# In[69]:


import pandas as pd


# In[71]:


def all_pages():
    movies_dict={
        'title':[],
        'duration':[],
        'rating':[],
        'year':[],
    }
  # We have to scrap more than one page so we want urls of all pages with the help of loop we can get all urls
    for i in range(1,2000,100):
       
        try:
            url = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&count=100&start='+str(i)+'&ref_=adv_next'
            response = requests.get(url)
        except:
            break
        
        if response.status_code != 200:
            break

        doc = BeautifulSoup(response.text, 'html.parser')
        titles = get_movie_titles(doc)
        ratings = get_movie_rating(doc)
        years = get_movie_year(doc)
        

        for i in range(len(titles)):
            movies_dict['title'].append(titles[i])
            movies_dict['rating'].append(ratings[i])
            movies_dict['year'].append(years[i])
        
    return pd.DataFrame(movies_dict)


# In[77]:


movies_dict={
    'title':titles,
    'rating':ratings,
    'year':years,
}


# In[78]:


df = pd.DataFrame(movies_dict)
df

