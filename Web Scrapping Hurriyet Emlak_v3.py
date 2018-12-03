# # This is a Capstone Project for Data Science course given in Roermond, NL.

# coding: utf-8

# I did not prefer to wrap results as string object in this project. 
# But if you want to work on strings to wrap the features you can return results string by using str function.

# for i in range(0,len(results)):
#     results[i] = str(results[i])
# str_res

# In[65]:

# First, necessary libraries are imported.
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup

# Global variables are defined.
list_id= []
price = []
date = []
area = []
owner = []
room = []
seller = []
adres = []
title = []

# A for loop is set in order to scrape ads from hurriyetemlak.com. 
for j in range():
    
    r = requests.get("https://www.hurriyetemlak.com/konut-satilik/villa/listeleme?pageSize=50&view=catalog&page={}".format(j))

    soup = BeautifulSoup(r.text,'html.parser')
    results = soup.find_all("a", attrs={'class':'overlay-link'})

# Each tag belong to an ad is compiled into the corresponding list.
    for tag in results :
        price.append(tag.get('data-price'))
        date.append(tag.get('data-date'))
        area.append(tag.get('data-meter'))
        owner.append(tag.get('data-owner'))
        room.append(tag.get('data-room'))
        seller.append(tag.get('data-seller-type'))
        adres.append(tag.get('href'))
        title.append(tag.get('title'))
        list_id.append(tag.get('data-listing-id'))

        # Lists above are merged into a dictionary.
        records={"list_id":list_id,"title": title, "price": price, "date":date, "area-m2": area, "owner":owner, "room": room, "seller": seller, "adres":adres, }
        
        #w = csv.writer(open("hurriyet.csv", "w"))

        #for key, val in records.items():

            #w.writerow([key, val])
        df = pd.DataFrame(records)
        # The dictionary is exported into a txt file named "?hurriyet.txt", where ? is the number of the web page that is scraped. 
        df.to_csv("{}hurriyet.txt".format(j))

#df.tail(20)


# In[16]:


#df.isnull().sum()


# In[17]:

# Aşağıdaki satır tekrar olmuş. ya yukarıdan ya da buradan silinebilir...
# import pandas as pd 

df=pd.read_csv("520hurriyet.txt") #neden 520 onu anlamadım???

for i in range(0,len(df.iloc[:,1])): 
               
    if df.iloc[i,1][0:5] == "https":
        df.loc[i,"adres"] = "New project without adres info"
               
    else:
        try:
            df.iloc[i,1] = "-".join(df.iloc[i,1].replace("/konut-satilik/","").replace("-emlakcidan-villa/detay","").replace("-sahibinden-villa/detay","").split("/"))
            df.iloc[i,1] = (str(df.iloc[i,1]))[0:-9]
            adres_list = (df.iloc[i,1].split("-"))
            df.loc[i,"şehir"]= adres_list[0]
            df.loc[i,"ilçe"]= adres_list[1]
            df.loc[i,"mahalle"]= adres_list[2]
        except:
            continue

df=df.dropna(subset=['list_id'])
 
df= df.drop(["Unnamed: 0"],axis=1)               

df.reset_index()

df.to_csv("520hurriyet_inorder.csv", index=False)


# In[42]:


#df.isnull().sum()


# In[11]:


#df.to_csv("50hurriyet_inorder.csv", index=False)


# 
# #import pandas as pd
# df1=pd.read_csv("50hurriyet_inorder.csv")
# df2=pd.read_csv("100hurriyet_inorder.csv")
# df3=pd.read_csv("150hurriyet_inorder.csv")
# df4=pd.read_csv("250hurriyet_inorder.csv")
# df5=pd.read_csv("350hurriyet_inorder.csv")
# df6=pd.read_csv("450hurriyet_inorder.csv")
# df7=pd.read_csv("520hurriyet_inorder.csv")

# In[1]:


#df2.sort_values(by=["şehir"])

