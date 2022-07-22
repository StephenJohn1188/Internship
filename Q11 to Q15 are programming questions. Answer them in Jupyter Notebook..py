#!/usr/bin/env python
# coding: utf-8

# Write a python program to find the factorial of a number.

# In[7]:


A=input("Enter the Number: ")
B = int(A)
factorial=1
if B<0:
    print("Factorial does not exist")
elif B==0:
    print("Factorial of 0 is 1")
else:
    for i in range (1,B+1):
        factorial = factorial*i
    print("The factorial of",B,"is",factorial)


# Write a python program to find whether a number is prime or composite.

# In[9]:


X = int(input("Enter any number : "))
if X > 1:
    for i in range(2, X):
        if (X % i) == 0:
            print(X, "is NOT a prime number")
            break
    else:
        print(X, "is a PRIME number")
elif X == 0 or 1:
    print(X, "is a neither prime NOR composite number")
else:
    print(X, "is NOT a prime number it is a COMPOSITE number")


# Write a python program to check whether a given string is palindrome or not.

# In[20]:


def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
s = input('Enter the string: ')
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")


# Write a Python program to get the third side of right-angled triangle from two given sides.

# In[18]:


#took some reference from internet

def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# Write a python program to print the frequency of each of the characters present in a given string.

# In[ ]:


A= input("Enter the string: ")
all_freq = {}
for i in A:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("The Count of characters is :\n "+  str(all_freq))


# In[ ]:




