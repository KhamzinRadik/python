# -*- coding: cp1251 -*-

import random

spisok=[random.randint(1, 10) for x in range (10)]
print (spisok)
kort=()
spisok_kort=[]
for i in range (0,len(spisok),+2):
    
    kort=spisok[i],spisok[i+1]
    spisok_kort.append(kort)
    
print(spisok_kort)