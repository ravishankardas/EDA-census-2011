#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats


# In[2]:


data = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')


# In[3]:


popdata = data[['Level','Name','TOT_M','TOT_F']].copy()


# In[4]:


popdata = popdata[popdata['Level']!='DISTRICT'].copy()


# In[5]:


popdata.drop_duplicates(subset ="Name",keep = 'first', inplace = True)


# In[6]:


rslt_df = popdata.copy(deep=True)


# In[7]:


rslt_df['Name'] = rslt_df['Name'].str.lower()


# In[8]:


rslt_df.sort_values("Name", axis = 0, ascending = True,inplace = True)


# In[9]:


rslt_df.rename(columns = {'Name':'State'}, inplace = True)


# In[10]:


rslt_df.reset_index(inplace=True)


# In[11]:


data2 = pd.read_excel('DDW-C18-0000.xlsx')


# In[12]:


new_col = ['state_code','District','Area','Total','Age','S_persons','S_males','S_females','T_persons','T_males','T_females']


# In[13]:


data2.columns = new_col


# In[14]:


data2 = data2.iloc[5:]


# In[15]:


new_data2 = data2.copy(deep=True)


# In[16]:


new_data2


# In[17]:


new_data2 = new_data2.drop(['District','Total','Age','S_persons','T_persons'],axis=1)


# In[18]:


new_data2.drop_duplicates(subset ="Area",keep = 'first', inplace = True)


# In[19]:


fin_data2 = new_data2.copy()


# In[20]:


fin_data2['Area'] = fin_data2['Area'].str.lower()


# In[21]:


fin_data2.sort_values("Area", axis = 0, ascending = True,inplace = True)


# In[22]:


fin_data2.rename(columns = {'Area':'State'}, inplace = True)


# In[23]:


fin_data2.reset_index(inplace=True)


# In[24]:


fin_data2.at[0,'State'] = 'andaman and nicobar islands'


# In[25]:


fin_data2.at[25,'State'] = 'delhi'


# In[26]:


fin_data2.at[14,'State'] = 'jammu and kashmir'


# In[27]:


int_df = pd.merge(rslt_df, fin_data2, how ='inner', on =['State'])


# In[28]:


int_df = int_df.drop(['index_x','Level','index_y',],axis=1)


# In[29]:


int_df['exactly_one_male'] = int_df['TOT_M'] - int_df['S_males']
int_df['exactly_one_female'] = int_df['TOT_F'] - int_df['S_females']


int_df['exactly_two_male'] = int_df['S_males'] - int_df['T_males']
int_df['exactly_two_female'] = int_df['S_females'] - int_df['T_females']


# In[30]:


int_df['exactly_one_male_ratio'] = (int_df['exactly_one_male']/int_df['TOT_M'])
int_df['exactly_one_female_ratio'] = (int_df['exactly_one_female']/int_df['TOT_F'])

int_df['exactly_two_male_ratio'] = (int_df['exactly_two_male']/int_df['TOT_M'])
int_df['exactly_two_female_ratio'] = (int_df['exactly_two_female']/int_df['TOT_F'])


# In[31]:


int_df['three_male_ratio'] = (int_df['T_males']/int_df['TOT_M'])
int_df['three_female_ratio'] = (int_df['T_females']/int_df['TOT_F'])


# In[32]:


int_df = int_df.drop(['T_males','S_males','S_females','T_females','exactly_one_male','exactly_one_female','exactly_two_male','exactly_two_female',],axis=1)


# In[33]:


int_df.sort_values("state_code", axis = 0, ascending = True,inplace = True)


# In[34]:


one = int_df[['state_code','TOT_M','TOT_F','exactly_one_male_ratio','exactly_one_female_ratio']].copy()
two = int_df[['state_code','TOT_M','TOT_F','exactly_two_male_ratio','exactly_two_female_ratio']].copy()
three = int_df[['state_code','TOT_M','TOT_F','three_male_ratio','three_female_ratio']].copy()


# In[35]:


p_values_one = []
p_values_two = []
p_values_three = []


# In[36]:


for i in range(0,36):
    the = one.iloc[i].to_list()
    s,p = stats.ttest_1samp([the[3],the[4]],the[1]/the[2])
    p_values_one.append(p)
    
    the = two.iloc[i].to_list()
    s,p = stats.ttest_1samp([the[3],the[4]],the[1]/the[2])
    p_values_two.append(p)
    
    the = three.iloc[i].to_list()
    s,p = stats.ttest_1samp([the[3],the[4]],the[1]/the[2])
    p_values_three.append(p)
    


# In[37]:


one['p-value'] = p_values_one
two['p-value'] = p_values_two
three['p-value'] = p_values_three


# In[38]:


one = one.drop(['TOT_M','TOT_F'],axis=1)
two = two.drop(['TOT_M','TOT_F'],axis=1)
three = three.drop(['TOT_M','TOT_F'],axis=1)


# In[39]:


one['exactly_one_male_ratio'] = one['exactly_one_male_ratio']*100
one['exactly_one_female_ratio'] = one['exactly_one_female_ratio']*100

two['exactly_two_male_ratio'] = two['exactly_two_male_ratio']*100
two['exactly_two_female_ratio'] = two['exactly_two_female_ratio']*100

three['three_male_ratio'] = three['three_male_ratio']*100
three['three_female_ratio'] = three['three_female_ratio']*100


# In[40]:


one.rename(columns = {'state_code':'state/ut','exactly_one_male_ratio':'male-percentage-one','exactly_one_female_ratio':'female-percentage-one',}, inplace = True)
two.rename(columns = {'state_code':'state/ut','exactly_two_male_ratio':'male-percentage-two','exactly_two_female_ratio':'female-percentage-two',}, inplace = True)
three.rename(columns = {'state_code':'state/ut','three_male_ratio':'male-percentage-three','three_female_ratio':'female-percentage-three',}, inplace = True)


# In[41]:


one.to_csv('gender-india-a.csv',index=False)
two.to_csv('gender-india-b.csv',index=False)
three.to_csv('gender-india-c.csv',index=False)


# In[ ]:




