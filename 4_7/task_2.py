# -*- coding: cp1251 -*-
import random

namber = int(input("input namber: "))
qwe=[random.randint(0,namber-1) for _ in  range (10)]
qwe=[(1 if x%2==0 else x%5 ) for x in qwe]

print (qwe)

