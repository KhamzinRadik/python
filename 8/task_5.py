# -*- coding: cp1251 -*-

nice_list = [1, 2, [3, 4], [[5, 6, 7],
           [8, 9, 10]], [[11, 12, 13],
             [14, 15], [16, 17, 18]]]
def izvlechenie (nice_list,lst=[]): 
    for arg in nice_list: 
        if isinstance(arg, int):#������� ����� n  �� ��� ��� �������� ���� ����������� ���� ����
            lst.append(arg)
            
        if isinstance (arg, list):#���� �� ��. ���� ���������� �� �� �� ��������
            izvlechenie(arg)
    return lst



print (izvlechenie(nice_list))