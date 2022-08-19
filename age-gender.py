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


new_data2 = new_data2[new_data2['Total']=='Total'].copy()


# In[8]:


two_data = new_data2.copy(deep=True)


# In[9]:


new_data2 = new_data2.drop(['District','S_persons','Total','S_males','S_females','T_persons'],axis=1)


# In[10]:


data1 = pd.read_excel('DDW-0000C-13.xls')


# In[11]:


new_col2 = ['Table name','state code','District code','Area','Age','total_person','tot_male','tot_female','total_person_rural','tot_male_rural','tot_female_rural','total_person_urban','tot_male_urban','tot_female_urban']


# In[12]:


data1.columns = new_col2
data1 = data1.iloc[6:]


# In[13]:


data1 = data1[['state code','Area','Age','tot_male','tot_female']].copy()


# In[14]:


the_list = data1.Area.unique()


# In[15]:


a = [5,10,15,20,25,30,50,70]
b = [9,14,19,24,29,49,69,99]
final_male_sum = []
final_female_sum = []
for area in the_list:
    df = data1[data1['Area'] == area].copy()
    final_male_sum.append(df.iloc[0].tolist()[-2])
    final_female_sum.append(df.iloc[0].tolist()[-1])
    for i,j in zip(a,b):
        valf = 0
        valm=0
        for k in range(i,j+1):
            row = df.loc[df['Age'] == k].values.flatten().tolist()
            valf+=row[-1]
            valm+=row[-2]
        final_male_sum.append(valm)
        final_female_sum.append(valf)
    r = df[df['Age'] == 'Age not stated'].values.flatten().tolist()
    final_male_sum.append(r[-2])
    final_female_sum.append(r[-1])


# In[16]:


len(final_male_sum)


# In[17]:


new_data2['male_row'] = final_male_sum
new_data2['female_row'] = final_female_sum


# In[18]:


new_data2 = new_data2[new_data2['Age']!='Total'].copy()


# In[19]:


new_data2['male_ratio'] = new_data2['T_males']/new_data2['male_row']
new_data2['female_ratio'] = new_data2['T_females']/new_data2['female_row']


# In[20]:


three_males = new_data2[['state','Area','Age','T_males','male_ratio']].copy()
three_females = new_data2[['state','Area','Age','T_females','female_ratio']].copy()


# In[21]:


three_males['max_column'] = three_males.groupby(['Area'])['male_ratio'].transform('max')
three_females['max_column'] = three_females.groupby(['Area'])['female_ratio'].transform('max')


# In[22]:


three_males = three_males[three_males['male_ratio'] == three_males['max_column']].copy()
three_females = three_females[three_females['female_ratio'] == three_females['max_column']].copy()


# In[23]:


three_males = three_males[['state','Age','T_males','male_ratio']].copy()
three_females = three_females[['state','Age','T_females','female_ratio']].copy()


# In[24]:


three_males.pop('T_males')


# In[25]:


three_females.pop('T_females')


# In[26]:


three_males = three_males.rename(columns={'male_ratio':'male-ratio-of-3','Age': 'male-age-group'})
three_females = three_females.rename(columns={'female_ratio':'female-ratio-of-3','Age': 'female-age-group'})


# In[27]:


res = pd.merge(three_males, three_females, on='state', how='outer')


# In[28]:


res.columns = ['state/ut','age-group-males','ratio-males-3','age-group-females','ratio-females-3']


# In[29]:


res.to_csv('age-gender-c.csv',index=False)


# In[30]:


two_data = two_data.drop(['District', 'S_persons','T_persons'], axis = 1)


# In[31]:


one_data = two_data[['state','Area','Age','S_males','S_females']].copy()


# In[32]:


two_data['exactly_two_male'] = two_data['S_males'] - two_data['T_males']
two_data['exactly_two_female'] = two_data['S_females'] - two_data['T_females']


# In[33]:


two_data = two_data.drop(['S_males', 'S_females','T_males','T_females'], axis = 1)


# In[34]:


two_data['male_col'] = final_male_sum
two_data['female_col'] = final_female_sum


# In[35]:


two_data = two_data[two_data['Age']!='Total'].copy()


# In[36]:


two_data['male_ratio'] = two_data['exactly_two_male']/two_data['male_col']
two_data['female_ratio'] = two_data['exactly_two_female']/two_data['female_col']


# In[37]:


two_data = two_data[['state','Area','Age','male_ratio','female_ratio']].copy()


# In[38]:


male_a = two_data[['state','Area','Age','male_ratio']].copy()
female_a = two_data[['state','Area','Age','female_ratio']].copy()


# In[39]:


male_a['max_column'] = male_a.groupby(['Area'])['male_ratio'].transform('max')
female_a['max_column'] = female_a.groupby(['Area'])['female_ratio'].transform('max')


# In[40]:


male_a = male_a[male_a['male_ratio'] == male_a['max_column']].copy()
female_a = female_a[female_a['female_ratio'] == female_a['max_column']].copy()


# In[41]:


male_a.pop('max_column')
female_a.pop('max_column')
male_a.pop('Area')
female_a.pop('Area')


# In[42]:


male_a = male_a.rename(columns={'male_ratio':'male-ratio-of-2','Age': 'male-age-group'})
female_a = female_a.rename(columns={'female_ratio':'female-ratio-of-2','Age': 'female-age-group'})


# In[43]:


result = pd.merge(male_a, female_a, on='state', how='outer')


# In[44]:


result.columns = ['state/ut','age-group-males','ratio-males-2','age-group-females','ratio-females-2']


# In[45]:


result.to_csv('age-gender-b.csv',index=False)


# In[46]:


one_data['male'] = final_male_sum


# In[47]:


one_data['female'] = final_female_sum


# In[48]:


one_data = one_data[one_data['Age']!='Total'].copy()


# In[49]:


one_data['exactly_one_male'] = one_data['male'] - one_data['S_males']
one_data['exactly_one_female'] = one_data['female'] - one_data['S_females']


# In[50]:


one_data = one_data[['state', 'Area', 'Age','exactly_one_male', 'exactly_one_female','male', 'female']].copy()


# In[51]:


one_data['male_ratio'] = one_data['exactly_one_male']/one_data['male']
one_data['female_ratio'] = one_data['exactly_one_female']/one_data['female']


# In[52]:


one_data = one_data[['state', 'Area', 'Age','male_ratio', 'female_ratio']].copy()


# In[53]:


male_one = one_data[['state','Area','Age','male_ratio']].copy()
female_one = one_data[['state','Area','Age','female_ratio']].copy()


# In[54]:


male_one['max_column'] = male_one.groupby(['Area'])['male_ratio'].transform('max')
female_one['max_column'] = female_one.groupby(['Area'])['female_ratio'].transform('max')


# In[55]:


male_one = male_one[male_one['male_ratio'] == male_one['max_column']].copy()
female_one = female_one[female_one['female_ratio'] == female_one['max_column']].copy()


# In[56]:


male_one.pop('max_column')
female_one.pop('max_column')


# In[57]:


male_one = male_one.rename(columns={'male_ratio':'male-ratio-of-1','Age': 'male-age-group'})
female_one = female_one.rename(columns={'female_ratio':'female-ratio-of-1','Age': 'female-age-group'})


# In[58]:


male_one.pop('Area')
female_one.pop('Area')


# In[59]:


final = pd.merge(male_one, female_one, on='state', how='outer')


# In[60]:


final.columns = ['state/ut','age-group-males','ratio-males-1','age-group-females','ratio-females-1']


# In[61]:


final.to_csv('age-gender-a.csv',index=False)

