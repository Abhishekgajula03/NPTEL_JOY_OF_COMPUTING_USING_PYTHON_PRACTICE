# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 09:47:51 2024

@author: Abhishek
"""
import string 
text=input().lower()
a=len(text)
output=''
for char in string.ascii_lowercase:#or you can also write down from a-z
    # check if char is present in the input text

    for i in range(a):
        if(char==text[i]):
            output+=char
print(output)

