# -*- coding: cp1251 -*-
from math import sqrt 

def square(num): 
    try: 
        if isinstance(num, (int, float)): 
            if num < 0: 
                raise ValueError('число должно быть положительным') 
            elif num == 0: 
                raise ZeroDivisionError('у нуля нет корня.') 
            else: 
                res = sqrt(num) 
                str_num = str(res) 
                if '.' in str_num[-2]: 
                    return int(res) 
                else: 
                    return res 
        else: 
            raise TypeError('ожидали число получили строку') 
    except (ValueError, ZeroDivisionError, TypeError) as exc: 
        return exc


lst = [16, 0, 25,-9, 4.7, 'asd'] 
for sym in lst: 
    result = square(sym) 
    print(f'Квадратный корень {sym} равен {result}')