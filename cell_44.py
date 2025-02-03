#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def prime_no(number):
  y = range(2,number)
  for i in y:
    if number % i == 0:
      return("not prime number")
  return("it is prime number")
x = prime_no(int(input("Please enter number to check prime number: ")))
print(x)

