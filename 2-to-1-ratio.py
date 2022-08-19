#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data2 = pd.read_excel('DDW-C18-0000.xlsx')


# In[3]:


new_col = ['state','District','Area','Total','Age','S_persons','S_males','S_females','T_persons','T_males','T_females']


# In[4]:


data2.columns = new_col


# In[5]:


data2 = data2.iloc[5:]


# In[6]:


new_data2 = data2.copy(deep=True)


# In[7]:


new_data2 = new_data2.drop(['District','Total','Age','S_males','S_females','T_males','T_females'],axis=1)


# In[8]:


new_data2.drop_duplicates(subset ="Area",keep = 'first', inplace = True)


# In[9]:


new_data2.reset_index(inplace=True)


# In[10]:


fin_data2 = new_data2.copy()


# In[11]:


fin_data2['Area'] = new_data2['Area'].str.lower()


# In[12]:


fin_data2.sort_values("Area", axis = 0, ascending = True,inplace = True)


# In[13]:


fin_data2.rename(columns = {'Area':'State','state':'state-code'}, inplace = True)


# In[14]:


fin_data2.reset_index(inplace=True)


# In[15]:


fin_data2['exactly_two'] = fin_data2['S_persons'] - fin_data2['T_persons']


# In[16]:


tot_data = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')


# In[17]:


tot_data = tot_data[['State','Level','Name','TOT_P']].copy()


# In[18]:


tot_data = tot_data[tot_data['Level']!='DISTRICT'].copy()


# In[19]:


tot_data.drop_duplicates(subset ="Name",keep = 'first', inplace = True)


# In[20]:


tot_data['Name'] = tot_data['Name'].str.lower()


# In[21]:


tot_data.pop('Level')
tot_data.pop('State')


# In[22]:


tot_data.rename(columns = {'Name':'State'}, inplace = True)


# In[23]:


result = pd.merge(fin_data2, tot_data, how ='inner', on =['State'])


# In[24]:


result['exactly_one'] = result['TOT_P']-result['S_persons']


# In[25]:


result = result.drop(['level_0','S_persons','T_persons','TOT_P'],axis=1)


# In[26]:


result['per'] = (result['exactly_two']/result['exactly_one'])*100


# In[27]:


result.sort_values("per", axis = 0, ascending = True,inplace = True, na_position ='last')


# In[28]:


top = result.head(3).copy()
bottom = result.tail(3).copy()


# In[29]:


top.sort_values("per", axis = 0, ascending = False,inplace = True, na_position ='last')


# In[30]:


final = pd.concat([top,bottom])


# In[31]:


final = final.drop(['index','exactly_two','exactly_one'],axis=1)


# In[32]:


final.pop('State')


# In[33]:


final.columns = ['state/ut','ratio']


# In[34]:


final.to_csv('2-to-1-ratio.csv',index=False)


# In[ ]:




