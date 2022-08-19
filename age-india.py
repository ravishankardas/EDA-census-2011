#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


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


new_data2


# In[8]:


new_data2 = new_data2.drop(['District','S_persons','S_males','S_females','T_males','T_females'],axis=1)


# In[9]:


fin_data2 = new_data2.loc[(new_data2['Total'] != 'Rural') & (new_data2['Total'] != 'Urban')]


# In[10]:


india = fin_data2[fin_data2['Area']=='INDIA'].copy()


# In[11]:


data1 = pd.read_excel('DDW-0000C-13.xls')


# In[12]:


new_col2 = ['Table name','state code','District code','Area','Age','total_person','tot_male','tot_female','total_person_rural','tot_male_rural','tot_female_rural','total_person_urban','tot_male_urban','tot_female_urban']


# In[13]:


data1.columns = new_col2
data1 = data1.iloc[6:]


# In[14]:


data1 = data1[['state code','District code','Area','Age','total_person']].copy()


# In[15]:


india2 = data1[data1['Area'] == 'India'].copy()


# In[16]:


india2[['total_person']] = india2[['total_person']].apply(pd.to_numeric)


# In[17]:


india


# In[18]:


final_sum = [86009580]
a = [5,10,15,20,25,30,50,70]
b = [9,14,19,24,29,49,69,99]
for i,j in zip(a,b):
    val = 0
    for k in range(i,j+1):
        row = india2.loc[india2['Age'] == k].values.flatten().tolist()
        val+=row[-1]
    final_sum.append(val)


# In[19]:


r = india2[india2['Age'] == 'Age not stated'].values.flatten().tolist()
final_sum.append(r[-1])


# In[20]:


india['new_col'] = final_sum


# In[21]:


india['percentage'] = (india['T_persons']/india['new_col'])*100


# In[22]:


india = india[1:].copy()


# In[23]:


india.sort_values("percentage", axis = 0, ascending = False,inplace = True, na_position ='last')


# In[24]:


fin_ind = india.iloc[0].to_frame().transpose()


# In[25]:


fin_ind = fin_ind[['state','Age','percentage']].copy()


# In[26]:


fin_ind = fin_ind.rename(columns={'state':'state/ut','Age': 'age-group'})


# In[27]:


fin_ind


# In[28]:


new_data2 = new_data2[new_data2['Area']!='INDIA'].copy()


# In[29]:


data1 = data1[data1['Area']!='India'].copy()


# In[30]:


data1['Area'] = data1['Area'].str.lower()


# In[31]:


new_data2['Area'] = new_data2['Area'].str.lower()


# In[32]:


len(data1.Area)


# In[33]:


the_list = data1.Area.unique()
the_list


# In[34]:


data1.iloc[0].tolist()[-1]


# In[35]:


a = [5,10,15,20,25,30,50,70]
b = [9,14,19,24,29,49,69,99]
final_sum = []
for area in the_list:
    df = data1[data1['Area'] == area].copy()
    final_sum.append(df.iloc[0].tolist()[-1])
    for i,j in zip(a,b):
        val = 0
        for k in range(i,j+1):
            row = df.loc[df['Age'] == k].values.flatten().tolist()
            val+=row[-1]
        final_sum.append(val)
    r = df[df['Age'] == 'Age not stated'].values.flatten().tolist()
    final_sum.append(r[-1])


# In[36]:


new_data2 = new_data2[new_data2['Total']!="Urban"].copy()


# In[37]:


new_data2 = new_data2[new_data2['Total']!="Rural"].copy()


# In[38]:


new_data2['row'] = final_sum


# In[39]:


new_data2 = new_data2[new_data2['Total']!=new_data2['Age']].copy()


# In[40]:


new_data2['percentage'] = (new_data2['T_persons']/new_data2['row'])*100


# In[41]:


type(new_data2.groupby('Area')['percentage'].max())


# In[42]:


new_data2['new_column'] = new_data2.groupby(['Area'])['percentage'].transform('max')


# In[43]:


new_data2 = new_data2[new_data2['percentage']==new_data2['new_column']].copy()


# In[44]:


new_data2 = new_data2[['state','Area','Age','percentage']].copy()


# In[45]:


new_data2.pop("Area")


# In[46]:


new_data2 = new_data2.rename(columns={'state':'state/ut','Age': 'age-group'})


# In[47]:


bigdata = new_data2.append(fin_ind, ignore_index=True)


# In[48]:


bigdata.sort_values("state/ut", axis = 0, ascending = True,inplace = True, na_position ='last')


# In[49]:


bigdata.to_csv('age-india.csv',index=False)


# In[50]:


bigdata

