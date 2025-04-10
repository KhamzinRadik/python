# -*- coding: cp1251 -*-
from math import sqrt 

def square(num): 
    try: 
        if isinstance(num, (int, float)): 
            if num < 0: 
                raise ValueError('����� ������ ���� �������������') 
            elif num == 0: 
                raise ZeroDivisionError('� ���� ��� �����.') 
            else: 
                res = sqrt(num) 
                str_num = str(res) 
                if '.' in str_num[-2]: 
                    return int(res) 
                else: 
                    return res 
        else: 
            raise TypeError('������� ����� �������� ������') 
    except (ValueError, ZeroDivisionError, TypeError) as exc: 
        return exc


lst = [16, 0, 25,-9, 4.7, 'asd'] 
for sym in lst: 
    result = square(sym) 
    print(f'���������� ������ {sym} ����� {result}')