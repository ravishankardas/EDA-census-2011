#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats


# In[2]:


data = pd.read_excel('DDW_PCA0000_2011_Indiastatedist.xlsx')


# In[3]:


popdata = data[['Level','Name','TRU','TOT_P']].copy()


# In[4]:


rslt_df = popdata[(popdata['Level'] == 'STATE') | (popdata['Level'] == 'India')].copy()


# In[5]:


ahem = rslt_df[(rslt_df['TRU'] == "Rural") | (rslt_df['TRU'] == "Urban")]


# In[6]:


rslt_df = ahem.copy(deep=True)


# In[7]:


rslt_df['Name'] = rslt_df['Name'].str.lower()


# In[8]:


rslt_df.pop('Level')


# In[9]:


rslt_df.rename(columns = {'Name':'State'}, inplace = True)


# In[10]:


rslt_df.reset_index(inplace=True)


# In[11]:


rslt_df.pop('index')


# In[12]:


rslt_df['TRU'] = rslt_df['TRU'].str.lower()


# In[13]:


rural1 = rslt_df[rslt_df['TRU']=='rural'].copy()
urban1 = rslt_df[rslt_df['TRU']=='urban'].copy()


# In[14]:


data2 = pd.read_excel('DDW-C19-0000.xlsx')


# In[15]:


new_col = ['state','District','Area','Total','Edu_level','S_persons','S_males','S_females','T_persons','T_males','T_females']


# In[16]:


data2.columns = new_col


# In[17]:


data2 = data2.iloc[5:]


# In[18]:


new_data2 = data2.copy(deep=True)


# In[19]:


new_data2['Area']= new_data2['Area'].str.lower()
new_data2['Total']= new_data2['Total'].str.lower()


# In[20]:


new_data2


# In[21]:


rural2 = new_data2[(new_data2['Total']=='rural') & (new_data2['Edu_level']=='Total')].copy()
urban2 = new_data2[(new_data2['Total']=='urban') & (new_data2['Edu_level']=='Total')].copy()


# In[22]:


rural2 = rural2.drop(['S_males','S_females','T_males','T_females'],axis=1)
urban2 = urban2.drop(['S_males','S_females','T_males','T_females'],axis=1)


# In[23]:


rural2.head()


# In[24]:


rural2.rename(columns = {'Area':'State','state':'state/ut'}, inplace = True)


# In[25]:


urban2.rename(columns = {'Area':'State','state':'state/ut'}, inplace = True)


# In[26]:


urban2.at[45,'State'] = 'jammu and kashmir'
urban2.at[189,'State'] = 'delhi'
urban2.at[861,'State'] = 'andaman and nicobar islands'


# In[27]:


rural2.at[37,'State'] = 'jammu and kashmir'
rural2.at[181,'State'] = 'delhi'
rural2.at[853,'State'] = 'andaman and nicobar islands'


# In[28]:


final_rural = pd.merge(rural1, rural2, how ='inner', on =['State'])


# In[29]:


final_rural = final_rural.drop(['Edu_level','TRU','Total',],axis=1)


# In[30]:


urban2.at[45,'Area'] = 'jammu and kashmir'
urban2.at[189,'Area'] = 'delhi'
urban2.at[861,'Area'] = 'andaman and nicobar islands'


# In[31]:


final_urban = pd.merge(urban1,urban2,how='inner',on=['State'])


# In[32]:


final_urban = final_urban.drop(['Edu_level','TRU','Total','Area'],axis=1)


# In[33]:


final_rural['one'] = final_rural['TOT_P'] - final_rural['S_persons']
final_rural['two'] = final_rural['S_persons'] - final_rural['T_persons']

final_urban['one'] = final_urban['TOT_P'] - final_urban['S_persons']
final_urban['two'] = final_urban['S_persons'] - final_urban['T_persons']


# In[34]:


final_urban.rename(columns = {'TOT_P':'tot_pop_urban','T_persons':'three',}, inplace = True)
final_rural.rename(columns = {'TOT_P':'tot_pop_rural','T_persons':'three',}, inplace = True)


# In[35]:


final_rural = final_rural.drop(['District','S_persons'],axis=1)
final_urban = final_urban.drop(['District','S_persons'],axis=1)


# In[36]:


final_rural['rural-one-ratio'] = final_rural['one']/final_rural['tot_pop_rural']
final_rural['rural-two-ratio'] = final_rural['two']/final_rural['tot_pop_rural']
final_rural['rural-three-ratio'] = final_rural['three']/final_rural['tot_pop_rural']


# In[37]:


final_urban['urban-one-ratio'] = final_urban['one']/final_urban['tot_pop_urban']
final_urban['urban-two-ratio'] = final_urban['two']/final_urban['tot_pop_urban']
final_urban['urban-three-ratio'] = final_urban['three']/final_urban['tot_pop_urban']


# In[38]:


final_urban = final_urban.drop(['one','three','two'],axis=1)
final_rural = final_rural.drop(['one','three','two'],axis=1)


# In[39]:


one_1 = final_rural[['state/ut','State','tot_pop_rural','rural-one-ratio']].copy()
one_2 = final_urban[['state/ut','State','tot_pop_urban','urban-one-ratio']].copy()


# In[40]:


one = pd.merge(one_1, one_2, how ='inner', on =['State'])


# In[41]:


one = one[['state/ut_x','State','tot_pop_urban','tot_pop_rural','urban-one-ratio','rural-one-ratio']].copy()


# In[42]:


one.iloc[0].to_list()


# In[43]:


one.head()


# In[44]:


one_p_values = []


# In[45]:


for i in range(0,36):
    the = one.iloc[i].to_list()
    r,p = stats.ttest_1samp([the[4],the[5]],the[2]/the[3])
    one_p_values.append(p)


# In[46]:


one['p-value']=one_p_values


# In[47]:


one.head()


# In[48]:


one = one.drop(['State','tot_pop_urban','tot_pop_rural'],axis=1)


# In[49]:


one['urban-one-ratio'] = one['urban-one-ratio']*100
one['rural-one-ratio'] = one['rural-one-ratio']*100


# In[50]:


one.rename(columns = {'state/ut_x':'state/ut','urban-one-ratio':'one-urban-percentage','rural-one-ratio':'one-urban-percentage'}, inplace = True)


# In[51]:


one.columns = ['state/ut','urban-percentage-one','rural-percentage-one','p-value']


# In[52]:


one.to_csv('geography-india-a.csv',index=False)


# In[53]:


two_1 = final_rural[['state/ut','State','tot_pop_rural','rural-two-ratio']].copy()
two_2 = final_urban[['state/ut','State','tot_pop_urban','urban-two-ratio']].copy()


# In[54]:


two = pd.merge(two_1, two_2, how ='inner', on =['State'])


# In[55]:


two = two[['state/ut_x','State','tot_pop_urban','tot_pop_rural','urban-two-ratio','rural-two-ratio']].copy()


# In[56]:


two_p_values = []


# In[57]:


for i in range(0,36):
    the = two.iloc[i].to_list()
    r,p = stats.ttest_1samp([the[4],the[5]],the[2]/the[3])
    two_p_values.append(p)


# In[58]:


two['p-value']=two_p_values


# In[59]:


two = two.drop(['State','tot_pop_urban','tot_pop_rural'],axis=1)


# In[60]:


two['urban-two-ratio'] = two['urban-two-ratio']*100
two['rural-two-ratio'] = two['rural-two-ratio']*100


# In[61]:


two.rename(columns = {'state/ut_x':'state/ut','urban-two-ratio':'two-urban-percentage','rural-two-ratio':'two-urban-percentage'}, inplace = True)


# In[62]:


two.head()


# In[63]:


two.columns = ['state/ut','urban-percentage-two','rural-percentage-two','p-value']


# In[64]:


two.to_csv('geography-india-b.csv',index=False)


# In[65]:


three_1 = final_rural[['state/ut','State','tot_pop_rural','rural-three-ratio']].copy()
three_2 = final_urban[['state/ut','State','tot_pop_urban','urban-three-ratio']].copy()


# In[66]:


three = pd.merge(three_1, three_2, how ='inner', on =['State'])


# In[67]:


three = three[['state/ut_x','State','tot_pop_urban','tot_pop_rural','urban-three-ratio','rural-three-ratio']].copy()


# In[68]:


three_p_values = []


# In[69]:


for i in range(0,36):
    the = three.iloc[i].to_list()
    r,p = stats.ttest_1samp([the[4],the[5]],the[2]/the[3])
    three_p_values.append(p)


# In[70]:


three['p-value']=three_p_values


# In[71]:


three = three.drop(['State','tot_pop_urban','tot_pop_rural'],axis=1)


# In[72]:


three['urban-three-ratio'] = three['urban-three-ratio']*100
three['rural-three-ratio'] = three['rural-three-ratio']*100


# In[73]:


three.rename(columns = {'state/ut_x':'state/ut','urban-three-ratio':'three-urban-percentage','rural-three-ratio':'three-urban-percentage'}, inplace = True)


# In[74]:


three.columns = ['state/ut','urban-percentage-three','rural-percentage-three','p-value']


# In[75]:


three.to_csv('geography-india-c.csv',index=False)

