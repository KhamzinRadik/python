# -*- coding: cp1251 -*-
import random

comand1=[round(random.uniform(5,10),2) for _ in  range (10)]
comand2=[round(random.uniform(5,10),2) for _ in  range (10)]
winer=[comand1[i] if comand1[i]>comand2[i] else comand2[i] for i in  range (10)]

print('comand1',comand1)
print('comand2',comand2)
print('winer',winer)