#!/usr/bin/env python
# coding: utf-8

# ### 1. Create this dictionary:
# **{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
#  using a dictionary comprehension.**

# In[3]:


dict={num:num**3 for num in range(0,5)}
dict


# ### 2. if the length of a word is even print "even!"

# In[25]:


word=input("Enter the word ")
if len(word)%2==0:
    print('even')


# In[2]:


st = 'Print every word in this sentence that has an even number of letters'


# In[30]:


def isEven(string):
    
    string=string.split(' ')
    
    for i in string:
        if (len(i)%2==0):
            print(i+' '+'has  even letters')
        
isEven(input("Enter the string : "))


# ### 3. Generate Password: 17 characters , minimum 1 Uppercase, 1 lowercase, 1 digits and 2 minimun special characters

# In[67]:


import random
import string
length=15
pas=""
all=""
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
spl=''

for i in range(2):
    spl=spl+''+(random.choice(string.punctuation))
all=lower+upper+digit

pas=random.sample(all,length)
password=''.join(random.sample(pas,len(pas)))

print(password+spl)



# # 4. you are given a list which is [6, 15, 5, 3, 5, 14, 3, 202, 34, 235, 555, 6]. You have to sort it such that the seventh element is greatest of all, second element is greater than last element and second last element is not greater than sum of 8 and sixth element

# In[91]:


import math


list1=[6,15,5,3,5,14,3,202,34,235,555,6]

a=max(list1)
list1[6]=a
if list1[1]<list1[-1]:
    for i in list1:
        if i>list1[1]:
            list1[1]=i
            break
if list1[-2]>list1[7]+list1[5]:
    for i in list1:
        if i<list1[7]+list1[5]:
            list1[-2]=i
            break
            
print(list1)
        
            
  
    


# In[ ]:





# ### 5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# In[40]:


for fizzbuzz in range(1,101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)    


# ### 6. Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program.

# In[81]:


import string
let=0
dig=0
str1=input("enter the string : ")
for i in str1:
    if i.isalpha():
        let+=1
    elif i.isdigit():
        dig+=1


print('the no of letters are {}. the number of digits are {}'.format(let,dig))


# ### 7. Exercise: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j
# 
# [[0, 0, 0, 0, 0],
#  [0, 1, 2, 3, 4],
#  [0, 2, 4, 6, 8]
#  ..............]]

# In[9]:


X = int(input("Enter number of rows: "))
Y = int(input("Enter number of columns: "))

li=[]
for i in range(X):
    row=[]
    for j in range(Y):
        
        row.append(i*j)
    
    li.append(row)
li


# In[ ]:





# ## 8. For this challenge,
# Create a bank account class that has two attributes:
# 
# owner balance and two methods:
# 
# deposit withdraw As an added requirement, withdrawals may not exceed the available balance.
# 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

# In[2]:


class Bankaccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("balance is : ",self.balance)
        
    def show_balance(self):
        print("balance is : ",self.balance)
    def withdraw(self,amount):
        if self.balance<amount:
            print("you cant withdraw")
        else:
            print("balance is : ",self.balance)
            self.balance-=amount
        
obj1=Bankaccount("rahman",2000)
obj1.deposit(2000)
obj1.withdraw(3000)


# In[ ]:




