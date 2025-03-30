# -*- coding: cp1251 -*-
import random


f_sq1=[random.randint(0,5-1) for _ in range (10)]
f_sq2=[random.randint(30,60) for _ in range (10)]
sq_3_cond =[('ded' if f_sq1[i_damage]+f_sq2[i_damage]>100
            else 'liv')
           for i_damage in range (10)]
print ('sq1',f_sq1)
print ('sq2',f_sq2)
print ('sq_3_cond',sq_3_cond)
