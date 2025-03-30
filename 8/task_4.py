# -*- coding: cp1251 -*-
def sum(*args, total=0): 
    for arg in args: 
        if isinstance(arg, (int, float)):
            
            total += arg 
        elif isinstance(arg, list): 
           
           total += sum(*arg) 
           print(*arg)
        
    return total 
print(sum([[1, 2, [3]], [1], 3]))   
print(sum(1, 2, 3, 4, 5))