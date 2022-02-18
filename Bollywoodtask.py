#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import operator

df = pd.read_csv(r'C:\Users\PRATEEK ANAND\Desktop\bollywood-1.csv')
print(df)


# In[2]:


#Question 1 

record = 0
with open(r'C:\Users\PRATEEK ANAND\Desktop\bollywood-1.csv') as csv_doc:
    csv_doc = csv.reader(csv_doc)
    for row in csv_doc:
        record += 1
print("the total number of records are: ",record-1)


# In[3]:


#Question 2

movies_no = []
releaseTime = df["ReleaseTime"].unique()
print("The different release times are: ",releaseTime)
for i in releaseTime:
    mov_no = 0
    for x in range(0, len(df["ReleaseTime"])):
        if(df["ReleaseTime"][x] == i):
            mov_no += 1
        else:
            continue
    movies_no.append(mov_no)
print("The number of movies in each release times are: ",movies_no)

print(df.sort_values(by=['ReleaseTime'],ascending=False)) 


# In[4]:


#Question 3


FS_mov_no =[]
for j in range(0,len(df["ReleaseTime"])):                                   
    if df["ReleaseTime"][j]=='FS':                                          
        FS_mov_no.append(df["Genre"][j])                           
    else:
        continue
c = dict(Counter(FS_mov_no))                                        
print(c)
print("Most released Genre during festive season is Drama and Thriller")


# In[5]:


# Question 4

tabulation = pd.crosstab(df.ReleaseTime, df.Genre)
print(tabulation)


# In[6]:


# Question 5
df["year"] = pd.DatetimeIndex(df["Release Date"])
print(df["year"])


Release_year = df["year"].unique()
year_13 = 0
year_14 = 0
year_15 = 0
for i in Release_year:
    if i == 2013:
        year_13 += 1
    elif i == 2014:
        year_14 += 1    
    else:
        year_15 += 1
        
print(year_13)
print(year_14)
print(year_15)

if year_13>year_14 and year_13>year_15:
    print("2013 has the most releases")
elif year_14>year_13 and year_14>year_15:
    print("2014 has the most releases")
else:
    print("2015 has the most releases")


# In[7]:


# Question 6

df["month"] = pd.DatetimeIndex(df["Release Date"]).month
high_month = []
for j in range(0,len(df["month"])):                                   
    if df["Budget"][j]>=30:                                          
        high_month.append(df["month"][j])                           
    else:
        continue
    coun = dict(Counter(high_month))                                                    
highest_month=max(coun.items(), key =operator.itemgetter(1))[0]                    
print("The month having the highest no of high budget movies(>= 30 crore) is:",highest_month)


# In[8]:


# Question 7

df["ROI"]=(df["BoxOfficeCollection"] - df["Budget"]) / df["Budget"]                     
sortv= df.sort_values(["ROI"])                                                          
print("Top 10 flop movies with minimum Return of Investment is:",sortv.head(10)) 


# In[9]:


# Question 8


# In[10]:


#Question 9

box_office = df["BoxOfficeCollection"]                                        
youtube_views = df["YoutubeViews"]                                            
correlation = box_office.corr(youtube_views)                           
if correlation > 0:                                                                  
    print("Yes it is correlated")
else:
    print("No it isnt correlated")


# In[ ]:




