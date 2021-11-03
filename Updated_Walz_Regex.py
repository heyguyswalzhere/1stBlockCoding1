#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("hi")


# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


print("happy Tuesday!")


# In[ ]:





# In[2]:


print("hello friends")


# # Pattern Matching and Regular Expressions

# isPhoneNumber code

# In[7]:


def isPhoneNumber(text):
    if len(text)!= 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


# In[2]:


def isPhoneNumber(text):
    if len(text)!= 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = ("my num is 111-111-1111 , 777-777-7777and it could be 222-222-2222 or also 333-333-3333")
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found:" + chunk)
print('done!')


# Creating Regex Objects

# In[1]:


import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("man i'm going to have to writee a lot of stuff on my own 222-222-2222 i wish that other thing had worked oh well 444-444-4444 i hope this works or i'll be really embarassed 555-555-555")
print('Phone number found: ' + mo.group())


# More Pattern Matching with Regular Expressions

# Grouping with Parentheses
# This allows me to just get the zip code if I want. The first group is first set in parentheses. And the second group is the last 7 digits...don't forget the characters in the string...

# In[5]:


import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
mo.group(1)
mo.group(2)


# # Grouping with Parentheses! 

# In[9]:


import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 111-111-1111")

mo.group(1)


# In[11]:


#see if we can make this look for an email pattern later...

import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 111-111-1111")

mo.groups()


# In[12]:


#gradYear, lastName, firstName = mo.groups()
#this could be the code we use to get the info we want
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)


# ### using character classses in regex objects
# 

# In[23]:


import re
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geeese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')


# ### making our own character classes

# In[24]:


import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Robocop eats baby food. BABY FOOD')


# In[28]:


#i'm going to figure this out...
import re 
mcnairyRegex = re.compile(r'[mcnairyMcnairy]')
mcnairyRegex.findall('walza@mcnairy.org')


# ### Email and Phone Number Regex project
# we will adapt this to our needs for mcnairy.org...we'll need to create a character class
# 

# In[32]:


#phoneAndEmail.py is what this file will be called when we run it
#finds emails and phone numbers in a large block of text in the clipboard
import pyperclip, re
phoneRegex = re.compile
phoneRegex = re.compile(r'''(
(\d{3}|\(d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)

#checks area code
#seperator...looks for dash
#first three digits
#seperator
#last four digits
#extension...we won't need this, but nice to have? 


                        
#TODO: CREATE EMAIL REGEX
                        


# In[ ]:




