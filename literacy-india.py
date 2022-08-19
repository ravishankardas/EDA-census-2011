#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data2 = pd.read_excel('DDW-C19-0000.xlsx')


# In[3]:


new_col = ['state','District','Area','Total','Edu-level','S_persons','S_males','S_females','T_persons','T_males','T_females']


# In[4]:


data2.columns = new_col


# In[5]:


data2 = data2.iloc[5:]


# In[6]:


new_data2 = data2.copy(deep=True)


# In[7]:


new_data2 = new_data2[new_data2['Total']=='Total'].copy()


# In[8]:


new_data2 = new_data2[['state','Area','Edu-level','T_persons']].copy()


# In[9]:


the = new_data2[new_data2['Area']=='INDIA']['Edu-level'].to_list()


# In[10]:


d = pd.read_excel('DDW-0000C-08.xlsx')


# In[11]:


d_col = ['table_name','state_code','dist_code','area_name','tot/urb/rur','age_group','tot_persons','tot_males','tot_females','illiterate_persons','illiterate_males','illiterate_females','literate_persons','literate_males','literate_females','literate_without_edu_level_persons','literate_without_edu_level_males','literate_without_edu_level_females','below_primary_persons','below_primary_males','below_primary_females','primary_persons','primary_males','primary_females','middle_persons','middle_males','middle_females','matric_persons','matric_males','matric_females','intermediate_persons','intermediate_males','intermediate_females','non_tech_diploma_persons','non_tech_diploma_males','non_tech_diploma_females','tech_diploma_persons','tech_diploma_males','tech_diploma_females','graduate_and_above_persons','graduate_and_above_males','graduate_and_above_females','unclassified_persons','unclassified_persons_males','unclassified_persons_females']


# In[12]:


d.columns = d_col


# In[13]:


d = d[6:]


# In[14]:


d = d[['state_code','area_name','tot/urb/rur','tot_persons','illiterate_persons','literate_persons','literate_without_edu_level_persons','below_primary_persons','primary_persons','middle_persons','matric_persons','intermediate_persons','non_tech_diploma_persons','tech_diploma_persons','graduate_and_above_persons','unclassified_persons']].copy()


# In[15]:


d = d[d['tot/urb/rur']=='Total'].copy()


# In[16]:


d.drop_duplicates(subset =["area_name",'tot/urb/rur'],keep = 'first', inplace = True)


# In[17]:


d['total_literate'] = d['literate_persons'] + d['unclassified_persons'] + d['literate_without_edu_level_persons']


# In[18]:


d['total_matric'] = d['matric_persons'] + d['intermediate_persons']+ d['non_tech_diploma_persons'] + d['tech_diploma_persons']


# In[19]:


code = d[['state_code','area_name']].copy()


# In[20]:


d = d[['state_code','area_name','illiterate_persons','total_literate','below_primary_persons','primary_persons','middle_persons','total_matric','graduate_and_above_persons']].copy()


# In[21]:


new_data2.head(10)


# In[22]:


new_data2 = new_data2[new_data2['Edu-level']!='Total']


# In[23]:


new_data2.head()


# In[24]:


d.head()


# In[25]:


col_list = ['state_code', 'area_name','illiterate', 'literate', 'literate but below primary','primary but below middle', 'middle but below matric/secondary', 'matric/secondary but below graduate', 'graduate and above']


# In[26]:


d.columns = col_list


# In[27]:


d.head()


# In[28]:


new_data2['Edu-level'] = new_data2['Edu-level'].str.lower()


# In[29]:


new_data2


# In[30]:


col_list = col_list[2:]


# In[31]:


def add(full):
    ahem = d[full].to_list()
    k=0
    for index, row in new_data2.iterrows():
        if row["Edu-level"]==full:
            new_data2.loc[index, 'total'] = ahem[k]
            k+=1


# In[32]:


for name in col_list:
    add(name)


# In[33]:


new_data2['percentage'] = (new_data2['T_persons']/new_data2['total'])*100


# In[34]:


new_data2['max_column'] = new_data2.groupby(['Area'])['percentage'].transform('max')


# In[35]:


new_data2 = new_data2[new_data2['percentage'] == new_data2['max_column']].copy()


# In[36]:


new_data2 = new_data2.drop(['Area','T_persons','total','max_column'],axis=1)


# In[37]:


new_data2 = new_data2.rename(columns={'state':'state/ut','Edu-level':'literacy-group'})


# In[38]:


new_data2.to_csv('literacy-india.csv',index=False)


# In[39]:


new_data2


# In[ ]:




