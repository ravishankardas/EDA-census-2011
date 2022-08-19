#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


andhra = pd.read_excel('andhra.XLSX',skiprows=5)
andman = pd.read_excel('andman.XLSX',skiprows=5)
arunachal = pd.read_excel('arunachal.XLSX',skiprows=5)
assam = pd.read_excel('assam.XLSX',skiprows=5)
bihar = pd.read_excel('bihar.XLSX',skiprows=5)
chandigarh = pd.read_excel('chandigarh.XLSX',skiprows=5)
chhatissgarh = pd.read_excel('chhatissgarh.XLSX',skiprows=5)
dadra = pd.read_excel('dadra.XLSX',skiprows = 5)


daman = pd.read_excel('daman.XLSX',skiprows=5)
delhi = pd.read_excel('delhi.XLSX',skiprows=5)
goa = pd.read_excel('goa.XLSX',skiprows=5)
gujarat = pd.read_excel('gujarat.XLSX',skiprows=5)
haryana = pd.read_excel('haryana.XLSX',skiprows=5)


himachal = pd.read_excel('himachal.XLSX',skiprows=5)
jammu = pd.read_excel('jammu.XLSX',skiprows=5)
arunachal = pd.read_excel('arunachal.XLSX',skiprows=5)
jharkhand = pd.read_excel('jharkhand.XLSX',skiprows=5)
karnatka = pd.read_excel('karnatka.XLSX',skiprows=5)

kerala = pd.read_excel('kerala.XLSX',skiprows=5)
lakshdweep = pd.read_excel('lakshdweep.XLSX',skiprows=5)
madhya = pd.read_excel('madhya.XLSX',skiprows=5)


maharashtra = pd.read_excel('maharashtra.XLSX',skiprows=5)
manipur = pd.read_excel('manipur.XLSX',skiprows=5)
meghalaya = pd.read_excel('meghalya.XLSX',skiprows=5)
mizoram = pd.read_excel('mizoram.XLSX',skiprows=5)
nagaland = pd.read_excel('nagaland.XLSX',skiprows=5)


odisha = pd.read_excel('odisha.XLSX',skiprows=5)
puddu  = pd.read_excel('puduu.XLSX',skiprows=5)
punjab = pd.read_excel('punjab.XLSX',skiprows=5)
rajashtan = pd.read_excel('rajasthan.XLSX',skiprows=5)
sikkim = pd.read_excel('sikkim.XLSX',skiprows=5)


tamilnadu = pd.read_excel('tamilnadu.XLSX',skiprows=5)
tripura = pd.read_excel('tripura.XLSX',skiprows=5)
up = pd.read_excel('UP.XLSX',skiprows=5)
uttrakhand = pd.read_excel('uttrakhand.XLSX',skiprows=5)
wb = pd.read_excel('WB.XLSX',skiprows=5)


# In[3]:


all_dfs = [andhra,andman,chandigarh,dadra,chhatissgarh,daman,delhi,goa,gujarat,haryana,himachal,jammu,arunachal,jharkhand,karnatka,kerala,lakshdweep,madhya,assam,bihar,maharashtra,manipur,meghalaya,mizoram,nagaland,odisha,puddu,punjab,rajashtan,sikkim,tamilnadu,tripura,up,uttrakhand,wb]


# In[4]:


len(all_dfs)


# In[5]:


new_col = ['state_code','state name','tot_code','tot_name','total','tot_males','tot_females','firstsub_code','firstsub_lang','firstsub_persons','firstsub_male','firstsub_female','secondsub_code','secondsub_lang','secondsub_persons','secondsub_male','secondsub_female']


# In[6]:


for df in all_dfs:
    df.columns = new_col
    df.fillna(0)


# In[7]:


north = [jammu,punjab,himachal,haryana,uttrakhand,delhi,chandigarh]
west = [rajashtan,gujarat,maharashtra,goa,dadra,daman]
central = [madhya,up,chhatissgarh]
east = [bihar,wb,odisha,jharkhand]
south = [karnatka,andhra,tamilnadu,kerala,lakshdweep,puddu]
north_east = [assam,sikkim,meghalaya,tripura,arunachal,manipur,nagaland,mizoram,andman]


# In[8]:


a = pd.concat(north)
b = pd.concat(west)
c = pd.concat(central)
d = pd.concat(east)
e = pd.concat(south)
f = pd.concat(north_east)
north_new = a.copy(deep=True)
west_new = b.copy(deep=True)
central_new = c.copy(deep=True)
east_new = d.copy(deep=True)
south_new = e.copy(deep=True)
north_east_new = f.copy(deep=True)


# In[9]:


north = a.sort_values(by=['total'],ascending=False)
west = b.sort_values(by=['total'],ascending=False)
central = c.sort_values(by=['total'],ascending=False)
east = d.sort_values(by=['total'],ascending=False)
south = e.sort_values(by=['total'],ascending=False)
north_east = f.sort_values(by=['total'],ascending=False)


# In[10]:


north =  north.groupby(['tot_name'])['total'].agg('sum').to_frame().reset_index().sort_values(by=['total',],ascending=False).head(3)['tot_name'].tolist()
west =  west.groupby(['tot_name'])['total'].agg('sum').to_frame().reset_index().sort_values(by=['total',],ascending=False).head(3)['tot_name'].tolist()
central =  central.groupby(['tot_name'])['total'].agg('sum').to_frame().reset_index().sort_values(by=['total',],ascending=False).head(3)['tot_name'].tolist()
east =  east.groupby(['tot_name'])['total'].agg('sum').to_frame().reset_index().sort_values(by=['total',],ascending=False).head(3)['tot_name'].tolist()
south =  south.groupby(['tot_name'])['total'].agg('sum').to_frame().reset_index().sort_values(by=['total',],ascending=False).head(3)['tot_name'].tolist()
north_east =  north_east.groupby(['tot_name'])['total'].agg('sum').to_frame().reset_index().sort_values(by=['total',],ascending=False).head(3)['tot_name'].tolist()


# In[11]:


north.insert(0,'North')
west.insert(0,'West')
central.insert(0,'Central')
east.insert(0,'East')
south.insert(0,'South')
north_east.insert(0,'North East')


# In[12]:


master_list = [north,west,central,east,south,north_east]


# In[13]:


result = pd.DataFrame(master_list,columns = ['region','language-1','language-2','language-3'])


# In[14]:


result = result.sort_values(by=['region'],ascending=True)


# In[15]:


result.to_csv('region_india_a.csv',index=False)


# In[16]:


north_new = north_new.fillna(0)
west_new = west_new.fillna(0)
central_new = central_new.fillna(0)
east_new = east_new.fillna(0)
south_new = south_new.fillna(0)
north_east_new = north_east_new.fillna(0)


# In[17]:


north_new = north_new[['state name','tot_name','total','firstsub_lang','firstsub_persons','secondsub_lang','secondsub_persons']].copy()
west_new = west_new[['state name','tot_name','total','firstsub_lang','firstsub_persons','secondsub_lang','secondsub_persons']].copy()
central_new = central_new[['state name','tot_name','total','firstsub_lang','firstsub_persons','secondsub_lang','secondsub_persons']].copy()
east_new = east_new[['state name','tot_name','total','firstsub_lang','firstsub_persons','secondsub_lang','secondsub_persons']].copy()
south_new = south_new[['state name','tot_name','total','firstsub_lang','firstsub_persons','secondsub_lang','secondsub_persons']].copy()
north_east_new = north_east_new[['state name','tot_name','total','firstsub_lang','firstsub_persons','secondsub_lang','secondsub_persons']].copy()


# In[18]:


def top_three(a):
    the = []
    for i in a['tot_name'].to_list():
        if type(i) == str:
            the.append(i)
    for i in a['firstsub_lang'].to_list():
        if type(i) == str:
            the.append(i)
    for i in a['secondsub_lang'].to_list():
        if type(i) == str:
            the.append(i)
    the = set(the)
    the_dict = {}
    for i in the:
        the_dict[i] = 0
    for index, row in a.iterrows():
        if row["tot_name"] in the:
            t = row["tot_name"]
            the_dict[t]+= row['total']
        if row["firstsub_lang"] in the:
            t = row["firstsub_lang"]
            the_dict[t]+= row['firstsub_persons']
        if row["secondsub_lang"] in the:
            t = row["secondsub_lang"]
            the_dict[t]+= row['secondsub_persons']
    ahem = pd.DataFrame(the_dict.items(), columns=['name', 'speaker'])
    return ahem.sort_values(by=['speaker'],ascending=False).head(3)['name'].to_list()        


# In[19]:


q = top_three(north_new)
w = top_three(west_new)
e = top_three(central_new)
r = top_three(east_new)
t = top_three(south_new)
y = top_three(north_east_new)
q.insert(0,'North')
w.insert(0,'West')
e.insert(0,'Central')
r.insert(0,'East')
t.insert(0,'South')
y.insert(0,'North East')


# In[20]:


master = [q,w,e,r,t,y]
res = pd.DataFrame(master,columns = ['region','language-1','language-2','language-3'])


# In[21]:


res = res.sort_values(by=['region'],ascending=True)


# In[22]:


res.to_csv('region-india_b.csv',index=False)


# In[23]:


res


# In[ ]:




