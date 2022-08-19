#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')


# In[3]:


popdata = data[['Level','Name','TOT_P']].copy()


# In[4]:


popdata.drop_duplicates(subset ="Name",keep = 'first', inplace = True)


# In[5]:


rslt_df = popdata[popdata['Level'] != 'DISTRICT'].copy()


# In[6]:


rslt_df.reset_index(inplace = True)


# In[7]:


rslt_df['Name'] = rslt_df['Name'].str.lower()


# In[8]:


rslt_df.sort_values("Name", axis = 0, ascending = True,inplace = True)


# In[9]:


rslt_df.rename(columns = {'Name':'State'}, inplace = True)


# In[10]:


rslt_df.reset_index(inplace=True)


# In[11]:


l1 = sum(rslt_df['TOT_P'].to_list())


# In[12]:


data2 = pd.read_excel('DDW-C18-0000.xlsx')


# In[13]:


new_col = ['state_code','District','Area','Total','Age','S_persons','S_males','S_females','T_persons','T_males','T_females']


# In[14]:


data2.columns = new_col


# In[15]:


data2 = data2.iloc[5:]


# In[16]:


new_data2 = data2.copy(deep=True)


# In[17]:


new_data2 = new_data2.drop(['District','Total','Age','S_males','S_females','T_males','T_females'],axis=1)


# In[18]:


new_data2.drop_duplicates(subset ="Area",keep = 'first', inplace = True)


# In[19]:


new_data2.reset_index(inplace=True)


# In[20]:


fin_data2 = new_data2.copy()


# In[21]:


fin_data2['Area'] = new_data2['Area'].str.lower()


# In[22]:


fin_data2.rename(columns = {'Area':'State'}, inplace = True)


# In[23]:


fin_data2.reset_index(inplace=True)


# In[24]:


fin_data2.at[35,'State'] = 'andaman and nicobar islands'


# In[25]:


fin_data2.at[7,'State'] = 'delhi'


# In[26]:


fin_data2.at[1,'State'] = 'jammu and kashmir'


# In[27]:


int_df = pd.merge(rslt_df, fin_data2, how ='inner', on =['State'])


# In[28]:


int_df['only_one'] = int_df['TOT_P'] - int_df['S_persons']


# In[29]:


int_df['exactly_two'] = int_df['S_persons'] - int_df['T_persons']


# In[30]:


int_df = int_df[['state_code','State','only_one','exactly_two','T_persons','TOT_P']]


# In[31]:


new_int_df = int_df.copy(deep=True)


# In[32]:


new_int_df['one_percentage'] = (int_df['only_one']/int_df['TOT_P'])*100


# In[33]:


new_int_df['two_percentage'] = (int_df['exactly_two']/int_df['TOT_P'])*100


# In[34]:


new_int_df['three_percentage'] = (int_df['T_persons']/int_df['TOT_P'])*100


# In[35]:


new_int_df = new_int_df[['state_code','one_percentage','two_percentage','three_percentage']].copy()


# In[36]:


new_int_df.sort_values("state_code", axis = 0, ascending = True,inplace = True)


# In[37]:


new_int_df.columns = ['state-code','percent-one','percent-two','percent-three']


# In[38]:


new_int_df.to_csv('percent-india.csv',index=False)


# In[ ]:




