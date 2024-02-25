# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 09:27:20 2024

@author: Abhishek
"""

c1_name=input()
c1_date=input()

c2_name=input()
c2_date=input()
c1_dob,c1_mob,c1_yob=int(c1_date[:2]),int(c1_date[3:5]),int(c1_date[6:])

c2_dob,c2_mob,c2_yob=int(c2_date[:2]),int(c2_date[3:5]),int(c2_date[6:])
younger=''
if c1_yob>c2_yob:
    younger=c1_name
elif c1_yob<c2_yob:
    yoounger=c2_name
else:
    if c1_mob>c2_mob:
        younger=c1_name
    elif c1_mob<c2_mob:
        younger=c2_name
    else:
        if c1_dob>c2_dob:
            younger=c1_name
        elif c1_dob<c2_dob:
            younger=c2_name
        else:
            if c1_name<c2_name:
                younger=c1_name
            else:
                younger=c2_name
print(younger)