# -*- coding: cp1251 -*-

nice_list = [1, 2, [3, 4], [[5, 6, 7],
           [8, 9, 10]], [[11, 12, 13],
             [14, 15], [16, 17, 18]]]
def izvlechenie (nice_list,lst=[]): 
    for arg in nice_list: 
        if isinstance(arg, int):#уровень равен n  на нем все элементы инты добавляются если инты
            lst.append(arg)
            
        if isinstance (arg, list):#если сл эл. лист перехгодим на др ур вложения
            izvlechenie(arg)
    return lst



print (izvlechenie(nice_list))