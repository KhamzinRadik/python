# -*- coding: cp1251 -*-

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
} 
tuple1=()
tuple2=[]
for i , y in (players.items()):
    
    tuple1 = (i+y)
    tuple2.append(tuple1)
print (f"Результат работы программы:" ,tuple2)