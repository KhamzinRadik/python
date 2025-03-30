# -*- coding: cp1251 -*-



def sort_lst(lst): 
    if len(lst) <= 1: 
        return lst 
    else: 
        support_elem = lst[-1] 
        
        left = [i_num for i_num in lst if i_num < support_elem] 
        center = [i_num for i_num in lst if i_num == support_elem] 
        right = [i_num for i_num in lst if i_num > support_elem] 
        return sort_lst(left) + center + sort_lst(right) 
       


lst = [5, 8, 9, 4, 7, 2, 9, 1, 7] 
print(sort_lst(lst))
