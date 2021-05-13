#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import libs for processing>
import pandas as pd
import numpy as np
import plotly.express as px

# In[7]:


cases = pd.read_csv("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv")
deaths = pd.read_csv('https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv')
recover = pd.read_csv("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv")


# In[8]:


# #lets drop the province/state col since it contains mostly nulls in all dfs
# cases.drop('Province/State' , axis =1 , inplace = True)
# recover.drop('Province/State' , axis =1 , inplace = True)
# deaths.drop('Province/State' , axis =1 , inplace = True)


# In[9]:


#renaming the country/region column withsingle word
country_rn = {"Country/Region":"Country"}
cases.rename(columns =country_rn , inplace = True)
recover.rename(columns =country_rn , inplace = True)
deaths.rename(columns =country_rn , inplace = True)


# In[10]:


#renaming the country/region column withsingle word
state_rn = {"Province/State":"state"}
cases.rename(columns =state_rn , inplace = True)
recover.rename(columns =state_rn , inplace = True)
deaths.rename(columns =state_rn , inplace = True)


# In[11]:


cases.head(2)


# In[12]:


cases.shape , deaths.shape , recover.shape


# In[13]:


# melt the date column

case_date = cases.columns[4:]
deaths_date = deaths.columns[4:]
recover_date = recover.columns[4:]


# In[14]:


# melt the colum
all_cases = pd.melt(cases, id_vars =['Country' , "Lat" , "Long"],
                    value_vars =case_date ,
                    var_name='date' ,
                    value_name="confirmed")

all_recover = pd.melt(recover, id_vars =['Country' , "Lat" , "Long"],
                    value_vars =recover_date ,
                    var_name='date' ,
                    value_name="recovery")

all_deaths = pd.melt(deaths, id_vars =[ 'Country' , "Lat" , "Long"],
                    value_vars =deaths_date ,
                    var_name='date' ,
                    value_name="deaths")


# In[15]:


all_deaths.tail()


# In[16]:


# merge the whole dataset
x = all_cases.merge(right=all_recover ,
                    how='left' ,
                    on = ['Country' , "Lat" , "Long" , "date"])

df =x.merge(right=all_deaths ,
                    how='left' ,
                    on = ['Country' , "Lat" , "Long" , "date"])


# In[17]:


df.isna().sum()


# In[18]:


# fill na for recovery with 0

df['recovery'].fillna(0 , inplace=True)


# In[20]:


# chanege date column to date time format

df['date'] = pd.to_datetime(df['date'])


# In[21]:


df.dtypes


# In[22]:


# change count to string

df['Country'] = df['Country'].astype('str')


# In[24]:


# get a new column active cases

df['active'] = df['confirmed']-df['deaths']-df['recovery']


# In[25]:


df.head()


# In[34]:


# group by date

df1 = df.groupby('date')[['confirmed' , 'recovery' , 'deaths' , "active"]].sum().reset_index(drop = False)


# In[35]:


df1.head()


# In[36]:


# frop by country and date

df2 = df.groupby(['Country' , 'date'])[['confirmed' , 'recovery' , 'deaths' , "active"]].sum().reset_index(drop = False)
