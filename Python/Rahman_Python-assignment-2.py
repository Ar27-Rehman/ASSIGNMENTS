#!/usr/bin/env python
# coding: utf-8

# #### 1.	Create a python program to find duplicate files by content. User will input path and it will scan all directories, sub-directories to find all duplicates files.
# **Delete the found duplicate file.
# [Hint: use hashlib]
# 

# In[ ]:


import os
import hashlib

def find_duplicates(root):
    hashes = {}
    duplicates = []
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            with open(full_path, 'rb') as file:
                file_hash = hashlib.sha256(file.read()).hexdigest()
            if file_hash in hashes:
                duplicates.append(full_path)
            else:
                hashes[file_hash] = full_path
    return duplicates

def delete_duplicates(duplicates):
    for path in duplicates:
        os.remove(path)
       # C:/Users/mabdulrahman/Desktop/assign/
        
path=input("Enter The Path : ")
dup=find_duplicates(path)
for i in dup:
    print(i)
    
deleted_dups=delete_duplicates(dup)
print("The deleted files are",deleted_dups)


# #### 2.	Generate random Password with exact length = 6, with minimum 1 uppercase, 2 lowercase, 2 digits, and remaining special characters.
# Using these packages [random, strings]
# 

# In[39]:


import string
import random

#length=int(input("ENTER THE LENGTH: "))
length=17
upper=string.ascii_uppercase

lower=string.ascii_lowercase

digits=string.digits

spl_char=string.punctuation

all=upper+lower+digits
password=''
password=random.sample(all,length-2)

for i in range(2):
    password.append(random.choice(spl_char))
random.shuffle(password)
password=''.join(password)

print("THE PASSWORD IS :",password)

    


# #### 3.	Create 2D array and update the same 2D array provided that every prime number position should be replaced by cube of the positioned number.

# In[60]:


import numpy as np

def is_prime(num):
    """
    Helper function to check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
arr = np.arange(1,31).reshape(5,6)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if is_prime(arr[i][j]):
            arr[i][j] = arr[i][j] ** 3

print(arr)


# #### 4.	Python program to get the sum of every cubed value and its previous integer. 
# 
# 

# In[135]:



n=int(input("Enter a number : "))
sum=0
for i in range(1,n+1):
    sum+=i**3+i-1
print(f"The sum of every cubed value and its previous integer is {sum}: ")


# #### 5.	Given two arrays, find their intersection. Examples:
# 
# #### Input:  arr1[] = [1, 3, 4, 5, 7]
# ####       arr2[] = [2, 3, 5, 6]
# 

# In[67]:


li1=[1,3,4,5,7]
li2=[2,3,5,6]
set1=set(li1)
set2=set(li2)
print(set1.intersection(set2))

'''
li1=[1,3,4,5,7]
li2=[2,3,5,6]
res=[]

for i in range(len(li1)):
    for j in range(len(li2)):
        if li1[i]==li2[j]:
            res.append(li1[i])
res
'''


# In[ ]:





# #### 6 Create a 7 x 7  2D array having only multiples of 7. And return the last element of the same

# array_2d = [[j*7 for j in range(1, 8)] for i in range(7)]
# 
# for i in range(7):
#     print(array_2d[i])
# 
# last_element = array_2d[6][6]
# print(f"Last element of the array is {last_element}.")
# 

# #### 7.	Checker Board Patten using Numpy:
# [   1   0   1   0   1   0   1
#     0   1   0   1   0   1   0
#     1   0   1   0   1   0   1
#     0   1   0   1   0   1   0
#     1   0   1   0   1   0   1  ]
# 

# In[103]:


array=np.zeros([5,7],dtype='int')

array[1::2,1::2]=1
array[::2,0::2]=1

array


# ####   8. 8.	Create a given Matrix:
# [  A,     B,     C,       D
#    E,      F,     G,       H
#     I,      a,      K,       L
#    M,    N,     o,       P
#    Q,     R,      S,       T
#    U,     0,     W,      O ]
#     Replace all the vowels by np.nan
#     A, E, I, O U  -- >  np.nan
#     Return the count of the missing values
# 

# In[127]:



import numpy as np
matrix = np.array([
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'a', 'K', 'L'],
    ['M', 'N', 'o', 'P'],
    ['Q', 'R', 'S', 'T'],
    ['U', '0', 'W', 'O']
])
a1=matrix
l=a1.flatten().tolist()
vow=['A','E','I','O','U']
for i in range(len(vow)):
    vow[i]=l.index(vow[i])
for i in vow:
    l[i]=np.nan
sol_arr=np.array(l)
sol_arr=sol_arr.reshape(4,6)
print(sol_arr)
li=sol_arr.flatten().tolist()
count=0

for i in range(len(li)):
    if li[i]=='nan':
        count+=1
print(count)


# In[ ]:




