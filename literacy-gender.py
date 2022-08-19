#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


d = pd.read_excel('DDW-0000C-08.xlsx')


# In[3]:


d_col = ['table_name','state_code','dist_code','area_name','tot/urb/rur','age_group','tot_persons','tot_males','tot_females','illiterate_persons','illiterate_males','illiterate_females','literate_persons','literate_males','literate_females','literate_without_edu_level_persons','literate_without_edu_level_males','literate_without_edu_level_females','below_primary_persons','below_primary_males','below_primary_females','primary_persons','primary_males','primary_females','middle_persons','middle_males','middle_females','matric_persons','matric_males','matric_females','intermediate_persons','intermediate_males','intermediate_females','non_tech_diploma_persons','non_tech_diploma_males','non_tech_diploma_females','tech_diploma_persons','tech_diploma_males','tech_diploma_females','graduate_and_above_persons','graduate_and_above_males','graduate_and_above_females','unclassified_persons','unclassified_persons_males','unclassified_persons_females']


# In[4]:


d.columns = d_col


# In[5]:


d = d[6:]


# In[6]:


d = d[['state_code','area_name','tot/urb/rur','illiterate_males','illiterate_females','literate_males','literate_females','literate_without_edu_level_males','literate_without_edu_level_females','below_primary_males','below_primary_females','primary_males','primary_females','middle_males','middle_females','matric_males','matric_females','intermediate_males','intermediate_females','non_tech_diploma_males','non_tech_diploma_females','tech_diploma_males','tech_diploma_females','graduate_and_above_males','graduate_and_above_females','unclassified_persons_males','unclassified_persons_females']].copy()


# In[7]:


d = d[d['tot/urb/rur']=='Total'].copy()


# In[8]:


d['total_literate_males'] = d['literate_males'] + d['unclassified_persons_males'] + d['literate_without_edu_level_males']
d['total_literate_females'] = d['literate_females'] + d['unclassified_persons_females'] + d['literate_without_edu_level_females']


# In[9]:


d['total_matric_males'] = d['matric_males'] + d['intermediate_males']+ d['non_tech_diploma_males'] + d['tech_diploma_males']
d['total_matric_females'] = d['matric_females'] + d['intermediate_females']+ d['non_tech_diploma_females'] + d['tech_diploma_females']


# In[10]:


data2 = pd.read_excel('DDW-C19-0000.xlsx')


# In[11]:


new_col = ['state','District','Area','Total','Edu-level','S_persons','S_males','S_females','T_persons','T_males','T_females']


# In[12]:


data2.columns = new_col


# In[13]:


data2 = data2.iloc[5:]


# In[14]:


new_data2 = data2.copy(deep=True)


# In[15]:


new_data2 = new_data2[new_data2['Total']=='Total'].copy()


# In[16]:


new_data2 = new_data2[new_data2['Edu-level']!='Total'].copy()


# In[17]:


d.drop_duplicates(subset =["area_name"],keep = 'first', inplace = True)


# In[18]:


three_data = new_data2[['state','Area','Edu-level','T_males','T_females']].copy()


# In[19]:


two_data = new_data2.copy(deep=True)


# In[20]:


one_data = new_data2[['state','Area','Edu-level','S_males','S_females']].copy()


# In[21]:


d.reset_index(inplace=True)


# In[22]:


d = d[['state_code', 'area_name', 'illiterate_males','illiterate_females','total_literate_males','total_literate_females','below_primary_males','below_primary_females', 'primary_males', 'primary_females','middle_males', 'middle_females','total_matric_males', 'total_matric_females','graduate_and_above_males','graduate_and_above_females', ]].copy()


# In[23]:


col_list = ['state_code', 'area_name','illiterate males','illiterate females', 'literate males', 'literate females', 'literate but below primary males', 'literate but below primary females', 'primary but below middle males', 'primary but below middle females', 'middle but below matric/secondary males', 'middle but below matric/secondary females', 'matric/secondary but below graduate males', 'matric/secondary but below graduate females', 'graduate and above males', 'graduate and above females']


# In[24]:


three_data.reset_index(inplace=True)


# In[25]:


d.columns = col_list


# In[26]:


text_male = 'male'
text_female = 'female'


# In[27]:


def add_male(full,first):
    ahem = d[full].to_list()
    k=0
    for index, row in three_data.iterrows():
        if row["Edu-level"]==first:
            three_data.loc[index, text_male] = ahem[k]
            k+=1


# In[28]:


def add_female(full,first):
    ahem = d[full].to_list()
    k=0
    for index, row in three_data.iterrows():
        if row["Edu-level"]==first:
            three_data.loc[index, text_female] = ahem[k]
            k+=1


# In[29]:


three_data['Edu-level'] = three_data['Edu-level'].str.lower()


# In[30]:


col_list = col_list[2:]


# In[31]:


for name in col_list:
    a = name.rsplit(' ', 1)[0]
    b = name.rsplit(' ', 1)[-1]
    if b == 'males':
        add_male(name,a)
    elif b == 'females':
        add_female(name,a)


# In[32]:


tot_data = three_data[['male','female']].copy()


# In[33]:


three_data['male_ratio'] = three_data['T_males']/three_data['male']
three_data['female_ratio'] = three_data['T_females']/three_data['female']


# In[34]:


three_males = three_data[['state','Area','Edu-level','male_ratio']].copy()
three_females = three_data[['state','Area','Edu-level','female_ratio']].copy()


# In[35]:


three_males['max_column'] = three_males.groupby(['Area'])['male_ratio'].transform('max')
three_females['max_column'] = three_females.groupby(['Area'])['female_ratio'].transform('max')


# In[36]:


three_males = three_males[three_males['male_ratio'] == three_males['max_column']].copy()
three_females = three_females[three_females['female_ratio'] == three_females['max_column']].copy()


# In[37]:


three_males = three_males.rename(columns={'state':'state/ut','Edu-level':'male-literacy-group','male_ratio':'male-ratio-of-3'})


# In[38]:


three_females = three_females.rename(columns={'state':'state/ut','Edu-level':'female-literacy-group','female_ratio':'female-ratio-of-3'})


# In[39]:


three_males.pop('max_column')
three_females.pop('max_column')


# In[40]:


final_three = pd.merge(three_males, three_females, on='Area', how='outer')


# In[41]:


final_three = final_three[['state/ut_x','male-literacy-group','male-ratio-of-3','female-literacy-group','female-ratio-of-3']].copy()


# In[42]:


final_three = final_three.rename(columns={'state/ut_x':'state/ut'})


# In[43]:


final_three.columns = ['state/ut','literacy-group-males', 'ratio-males-3','literacy-group-females', 'ratio-females-3']


# In[44]:


final_three.to_csv('literacy-gender-c.csv')


# In[45]:


two_data['exactly_two_male'] = two_data['S_males'] - two_data['T_males']
two_data['exactly_two_female'] = two_data['S_females'] - two_data['T_females']


# In[46]:


two_data = two_data[['state','Area','Edu-level','exactly_two_male','exactly_two_female']].copy()


# In[47]:


two_data['male'] = tot_data['male'].to_list()


# In[48]:


two_data['female'] = tot_data['female'].to_list()


# In[49]:


two_male = two_data[['state','Area','Edu-level','exactly_two_male','male']].copy()
two_female = two_data[['state','Area','Edu-level','exactly_two_female','female']].copy()


# In[50]:


two_male['male-ratio-of-2'] = two_male['exactly_two_male']/two_male['male']
two_female['female-ratio-of-2'] = two_female['exactly_two_female']/two_female['female']


# In[51]:


two_male['max_column'] = two_male.groupby(['Area'])['male-ratio-of-2'].transform('max')
two_female['max_column'] = two_female.groupby(['Area'])['female-ratio-of-2'].transform('max')


# In[52]:


two_male = two_male[two_male['male-ratio-of-2'] == two_male['max_column']].copy()
two_female = two_female[two_female['female-ratio-of-2'] == two_female['max_column']].copy()


# In[53]:


two_male = two_male[['state','Area','Edu-level','male-ratio-of-2']].copy()
two_female = two_female[['state','Area','Edu-level','female-ratio-of-2']].copy()


# In[54]:


two_male = two_male.rename(columns={'state':'state/ut','Edu-level':'male-literacy-group',})
two_female = two_female.rename(columns={'state':'state/ut','Edu-level':'female-literacy-group',})


# In[55]:


final_two = pd.merge(two_male, two_female, on='Area', how='outer')


# In[56]:


final_two.pop('state/ut_y')


# In[57]:


final_two = final_two.rename(columns={'state/ut_x':'state/ut',})


# In[58]:


final_two.pop('Area')


# In[59]:


final_two.columns = ['state/ut','literacy-group-males', 'ratio-males-2','literacy-group-females', 'ratio-females-2']


# In[60]:


final_two.to_csv('literacy-gender-b.csv',index=False)


# In[61]:


one_data['male'] = tot_data['male'].to_list()
one_data['female'] = tot_data['female'].to_list()


# In[62]:


one_data['exactly_one_male'] = one_data['male'] - one_data['S_males']
one_data['exactly_one_female'] = one_data['female'] - one_data['S_females']


# In[63]:


one_data = one_data.drop(['S_males','S_females'],axis=1)


# In[64]:


one_data['male-ratio-of-1'] = one_data['exactly_one_male']/one_data['male']
one_data['female-ratio-of-1'] = one_data['exactly_one_female']/one_data['female']


# In[65]:


one_male = one_data[['state','Area','Edu-level','male-ratio-of-1']].copy()
one_female = one_data[['state','Area','Edu-level','female-ratio-of-1']].copy()


# In[66]:


one_male['max_column'] = one_male.groupby(['Area'])['male-ratio-of-1'].transform('max')
one_female['max_column'] = one_female.groupby(['Area'])['female-ratio-of-1'].transform('max')


# In[67]:


one_male = one_male[one_male['male-ratio-of-1'] == one_male['max_column']].copy()
one_female = one_female[one_female['female-ratio-of-1'] == one_female['max_column']].copy()


# In[68]:


one_male.pop('max_column')
one_female.pop('max_column')


# In[69]:


one_male = one_male.rename(columns={'Edu-level':'male-literacy-group'})
one_female = one_female.rename(columns={'Edu-level':'female-literacy-group'})


# In[70]:


final_one = pd.merge(one_male, one_female, on='Area', how='outer')


# In[71]:


final_one = final_one.drop(['Area','state_y'],axis=1)


# In[72]:


final_one = final_one.rename(columns={'state_x':'state/ut'})


# In[73]:


final_one.columns = ['state/ut','literacy-group-males', 'ratio-males-1','literacy-group-females', 'ratio-females-1']


# In[74]:


final_one.to_csv('literacy-gender-a.csv',index=False)


# In[ ]:




