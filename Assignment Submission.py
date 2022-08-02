#!/usr/bin/env python
# coding: utf-8

# # 1)	Write a python program to display all the header tags from wikipedia.org

# In[20]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# # 2) Python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame..py

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


import requests


# In[4]:


topics=requests.get("https://www.imdb.com/search/title/?groups=top_100")


# In[5]:


content=topics.text


# In[6]:


content[:500]


# In[7]:


from bs4 import BeautifulSoup


# In[9]:


doc = BeautifulSoup(topics.text,'html.parser')


# In[10]:


doc.find('title')


# In[71]:


def get_movie_titles(doc):
    
    selection_class="lister-item-header"
    movie_title_tags=doc.find_all('h3',{'class':selection_class})
    movie_titles=[]

    for tag in movie_title_tags:
        title = tag.find('a').text
        movie_titles.append(title)
        
        
    return movie_titles


# In[72]:


titles = get_movie_titles(doc)


# In[13]:


def get_movie_rating(doc):
    rating_selector="inline-block ratings-imdb-rating"            
    movie_rating_tags=doc.find_all('div',{'class':rating_selector})
    movie_rating_tagss=[]
    for tag in movie_rating_tags:
        movie_rating_tagss.append(tag.get_text().strip())
    return movie_rating_tagss


# In[14]:


ratings = get_movie_rating(doc)
ratings[:5]


# In[15]:


def get_movie_year(doc):
    year_selector = "lister-item-year text-muted unbold"           
    movie_year_tags=doc.find_all('span',{'class':year_selector})
    movie_year_tagss=[]
    for tag in movie_year_tags:
        movie_year_tagss.append(tag.get_text().strip()[1:5])
    return movie_year_tagss


# In[16]:


years = get_movie_year(doc)
years[:5]


# In[17]:


import pandas as pd


# In[19]:


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


# In[20]:


movies_dict={
    'title':titles,
    'rating':ratings,
    'year':years,
}


# In[21]:


df = pd.DataFrame(movies_dict)
df


# # 3) Python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame..py

# In[101]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[102]:


import requests


# In[103]:


topics=requests.get("https://www.imdb.com/list/ls079077479/")


# In[104]:


content=topics.text


# In[105]:


content[:500]


# In[106]:


from bs4 import BeautifulSoup


# In[107]:


doc.find('title')


# In[112]:


def get_movie_titles(doc):
    
    selection_class="lister-item-header"
    movie_title_tags=doc.find_all('h3',{'class':selection_class})
    movie_titles=[]

    for tag in movie_title_tags:
        title = tag.find('a').text
        movie_titles.append(title)
        
        
    return movie_titles


# In[113]:


titles = get_movie_titles(doc)


# In[114]:


titles


# In[94]:


def get_movie_rating(doc):
    rating_selector="ipl-rating-star__rating"            
    movie_rating_tags=doc.find_all('div',{'class':rating_selector})
    movie_rating_tagss=[]
    for tag in movie_rating_tags:
        movie_rating_tagss.append(tag.get_text().strip())
    return movie_rating_tagss


# In[95]:


ratings = get_movie_rating(doc)
ratings[:5]


# In[115]:


def get_movie_year(doc):
    year_selector = "lister-item-year text-muted unbold"           
    movie_year_tags=doc.find_all('span',{'class':year_selector})
    movie_year_tagss=[]
    for tag in movie_year_tags:
        movie_year_tagss.append(tag.get_text().strip()[1:5])
    return movie_year_tagss


# In[116]:


years = get_movie_year(doc)
years[:5]


# In[117]:


import pandas as pd


# In[118]:


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


# In[119]:


movies_dict={
    'title':titles,
    'rating':ratings,
    'year':years,
}


# In[120]:


df = pd.DataFrame(movies_dict)
df


# # 4)	Write s python program to display list of respected former presidents of India

# In[19]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[4]:


from bs4 import BeautifulSoup
import requests


# In[6]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[7]:


soup=BeautifulSoup(page.content)
soup


# In[8]:


first_title=soup.find('h3')
first_title


# In[9]:


first_title=[]
for i in soup.find_all('h3'):
    first_title.append(i.text)
first_title


# In[10]:


Term=[]
for i in soup.find_all('p'):
    Term.append(i.text)
Term


# In[11]:


Detail=[]
for i in soup.find_all('div', class_="presidentListing"):
    Detail.append(i.text)
Detail


# In[12]:


import pandas as pd
df=pd.DataFrame({"PresidentiaL List":Detail})
df


# # a)	Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[13]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[14]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[15]:


country=BeautifulSoup(page.content)
country


# Country

# In[16]:


country_name=[]
for i in country.find_all('span',class_='u-hide-phablet'):
    country_name.append(i.text)
country_name


# In[17]:


match_no=[]
for i in country.find_all('td',class_='table-body__cell u-center-text'):
    match_no.append(i.text)
match_no


# In[18]:


rating_no=[]
for i in country.find_all('td',class_='table-body__cell u-text-right rating'):
    rating_no.append(i.text)
rating_no


# # b)	Top 10 ODI Bowlers along with the records of their team and rating.

# In[21]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
import requests
from bs4 import BeautifulSoup


# In[22]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
page


# In[23]:


country=BeautifulSoup(page.content)
country


# In[24]:


player_name=country.find('td',class_='table-body__cell rankings-table__name name')
player_name


# In[25]:


player_name.text


# In[26]:


player_name=[]
for i in country.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# In[27]:


Team=[]
for i in country.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# In[28]:


Rating=[]
for i in country.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[57]:


import pandas as pd
df=pd.DataFrame({"Player Name":player_name, "Team": Team, "Rating":Rating})
df.head(10)


# In[ ]:





# # c)	Top 10 ODI bowlers along with the records of their team and rating.

# In[30]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
page


# In[31]:


country=BeautifulSoup(page.content)
country


# In[32]:


player_name=[]
for i in country.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# In[33]:


Team=[]
for i in country.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# In[34]:


Rating=[]
for i in country.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[56]:


import pandas as pd
df=pd.DataFrame({"Team": Team, "Rating":Rating})
df.head(10)


# In[ ]:





# # A) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating

# In[37]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[38]:


country=BeautifulSoup(page.content)
country


# In[39]:


country_name=[]
for i in country.find_all('span',class_='u-hide-phablet'):
   country_name.append(i.text)
country_name


# In[40]:


Match=[]
for i in country.find_all('td',class_='table-body__cell u-center-text'):
  Match.append(i.text)
Match


# In[41]:


Rating=[]
for i in country.find_all('td',class_='table-body__cell u-text-right rating'):
  Rating.append(i.text)
Rating


# # B) Top 10 women’s ODI Batting players along with the records of their team and rating

# In[42]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
page


# In[43]:


country=BeautifulSoup(page.content)
country


# In[44]:


player_name=[]
for i in country.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# In[45]:


Team=[]
for i in country.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# In[46]:


Rating=[]
for i in country.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[55]:


import pandas as pd
df=pd.DataFrame({"Player Name":player_name, "Team": Team, "Rating":Rating})
df.head(10)


# In[ ]:





# # C) Top 10 women’s ODI all-rounder along with the records of their team and rating

# In[48]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
page


# In[49]:


country=BeautifulSoup(page.content)
country


# In[50]:


player_name=[]
for i in country.find_all('td',class_='table-body__cell rankings-table__name name'):
   player_name.append(i.text)
player_name


# In[51]:


Team=[]
for i in country.find_all('span',class_='table-body__logo-text'):
  Team.append(i.text)
Team


# In[52]:


Rating=[]
for i in country.find_all('td',class_='table-body__cell rating'):
  Rating.append(i.text)
Rating


# In[54]:


import pandas as pd
df=pd.DataFrame({"Player Name":player_name, "Team": Team, "Rating":Rating})
df.head(10)


# # a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world 

# In[58]:


page=requests.get('https://www.cnbc.com/world/?region=world')
page


# In[59]:


news=BeautifulSoup(page.content)
news


# In[60]:


Headline=[]
for i in news.find_all('div',class_='RiverHeadline-headline RiverHeadline-hasThumbnail'):
   Headline.append(i.text)
Headline


# In[61]:


Time=[]
for i in news.find_all('time'):
   Time.append(i.text)
Time


# In[62]:


url = "https://www.cnbc.com/world/?region=world"
webpage = requests.get(url) 
trav = BeautifulSoup(webpage.content, "html.parser")
for link in trav.find_all('a'):
    print(type(link), " ", link)


# # a python program to scrape the details of most downloaded articles from AI in last 90 days

# In[63]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[64]:


Books=BeautifulSoup(page.content)
Books


# In[65]:


Title=[]
for i in Books.find_all('h2'):
   Title.append(i.text)
Title


# In[66]:


Author=[]
for i in Books.find_all('span',class_="sc-1w3fpd7-0 pgLAT"):
   Author.append(i.text)
Author


# In[67]:


Date=[]
for i in Books.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
   Date.append(i.text)
Date


# In[68]:


import pandas as pd
df=pd.DataFrame({"Title":Title, "Author":Author, "Published Date":Date})
df


# # a python program to scrape mentioned details from dineout.co.in 

# In[70]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/welcome-back')
page


# In[71]:


soup=BeautifulSoup(page.content)
soup


# In[72]:


RN=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    RN.append(i.text)
    
RN


# In[73]:


price=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    price.append(i.text)
    
price


# In[74]:


location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
location


# In[75]:


images=[]
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
    
images


# In[76]:


RT=[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    RT.append(i.text)
    
RT


# In[77]:


import pandas as pd
df=pd.DataFrame({"Restaurant Name":RN, "Cusines":price, "Location":location, "Ratings":RT,"Images_Url":images})
df


# # a python program to scrape the details of top publications from Google Scholar 

# In[78]:


page=requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page


# In[79]:


book=BeautifulSoup(page.content)
book


# In[80]:


Rank=[]
for i in book.find_all('td',class_='gsc_mvt_p'):
   Rank.append(i.text)
Rank


# In[81]:


Pub=[]
for i in book.find_all('td',class_='gsc_mvt_t'):
   Pub.append(i.text)
Pub


# In[82]:


H5=[]
for i in book.find_all('a',class_='gs_ibl gsc_mp_anchor'):
   H5.append(i.text)
H5


# In[83]:


h5=[]
for i in book.find_all('span',class_='gs_ibl gsc_mp_anchor'):
   h5.append(i.text)
h5


# In[84]:


import pandas as pd
df=pd.DataFrame({"Rank":Rank,"Publication":Pub,"H5 Ixdex":H5,"H5 Median":h5})
df


# In[ ]:




