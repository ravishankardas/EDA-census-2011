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


new_data2.pop('index')


# In[11]:


fin_data2 = new_data2.copy()


# In[12]:


fin_data2['Area'] = new_data2['Area'].str.lower()


# In[13]:


fin_data2.sort_values("Area", axis = 0, ascending = True,inplace = True)


# In[14]:


fin_data2.rename(columns = {'Area':'State','state':'state/ut'}, inplace = True)


# In[15]:


fin_data2.reset_index(inplace=True)


# In[16]:


fin_data2.pop('index')


# In[17]:


fin_data2['exactly_two'] = fin_data2['S_persons'] - fin_data2['T_persons']


# In[18]:


fin_df = fin_data2.copy()


# In[19]:


fin_data2.pop('S_persons')


# In[20]:


fin_data2['ratio'] = fin_data2['T_persons']/fin_data2['exactly_two']


# In[21]:


fin_data2.pop('T_persons')


# In[22]:


fin_data2.pop('exactly_two')


# In[23]:


fin_data2.sort_values("ratio", axis = 0, ascending = False,inplace = True)


# In[24]:


dfa = fin_data2.head(3).copy()


# In[25]:


dfb = fin_data2.tail(3).copy()


# In[26]:


dfa


# In[27]:


dfb.sort_values("ratio", axis = 0, ascending = True,inplace = True)


# In[28]:


all_dfs = [dfa, dfb]


# In[29]:


for df in all_dfs:
    df.columns = ['state/ut','State', 'ratio']


# In[30]:


result = pd.concat(all_dfs).reset_index(drop=True)


# In[31]:


result.pop('State')


# In[32]:


result.to_csv('3-to-2-ratio.csv',index=False)


# In[33]:


result


# In[ ]:




