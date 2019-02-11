#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


filename = "employee_data.csv"
with open (filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#     next(csvreader, None)
    data = list(csvreader)


# In[3]:


print(data[0])
    


# In[4]:


header=["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
print(header)
    


# In[5]:


data[0]=header
print(data[0])


# In[6]:


del data[0]
# print(data)


# In[7]:


# Manipulate data
for row in data:
    # Break name out to two columns
    name = row[1]
    namelist = name.split()
    firstname=namelist[0]
    lastname=namelist[1]
#     print(firstname)
#     print(lastname)
    del row[1]
    row.insert(1,firstname)
    row.insert(2,lastname)


# In[8]:


# Modify Date
for row in data:
    b_date = row[3]
    splitdate = b_date.split("-")
    year = splitdate[0]
    month = splitdate[1]
    day = splitdate[2]
#     print(year)
#     print(month)
#     print(day)
    mod_date= (f"{month}/{day}/{year}")
    del row[3]
    row.insert(3,mod_date)
#     print(mod_date)


# In[9]:


# Modify SSN Number
for row in data:
    ssn = row[4]
    splitssn = ssn.split("-")
    splitssn[0]= "***"
    splitssn[1]= "**"
    modssn= (f"{splitssn[0]}-{splitssn[1]}-{splitssn[2]}")
    del row[4]
    row.insert(4,modssn)
#     print(modssn)


# In[10]:


#Modify State
us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT',
    'Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA',
    'Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA',
    'Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV',
    'New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND',
    'Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD',
    'Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV',
    'Wisconsin': 'WI','Wyoming': 'WY',
}
for row in data:
    state = row[5]
    abbrev_state = us_state_abbrev.get(state)
    del row[5]
    row.insert(5,abbrev_state)
# print(data)


# In[11]:


#Insert Header
data.insert(0,header)
# print(data)


# In[24]:


#Export to CSV file
filename = "employee_data_2.csv"
with open (filename, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter = csvwriter.writerows(data)

csvfile.close()


# In[ ]:




