#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import re

letter_list = []


# In[2]:


filename = open("raw_data/paragraph_1.txt", "r")
lines = filename.readlines()
str1 = " ".join(lines)
words = str1.split()
sentences = re.split("(?<=[.!?]) +",str1)
# print(words)
# print("-------------------------------------------------------------------------------------------------------------------")
# print(sentences)


# In[3]:


# Count number of words
word_count = len(words)

# Count total number of sentences
sent_count =len(sentences)

# Letter Count
for row in words:
    letter_count = len(words[0])
    letter_list.append(letter_count)
letter_count = sum(letter_list)/word_count

#Average sentence length in words
sent_length = word_count/sent_count


# In[4]:


#Print out summary
print("Paragraph Analysis")
print("-----------------------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sent_count}")
print(f"Approximate Letter Count: {letter_count}")
print(f"Approximate Sentence Length: {sent_length}")


# In[ ]:




