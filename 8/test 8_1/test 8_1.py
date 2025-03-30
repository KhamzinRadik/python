# -*- coding: cp1251 -*-



def power(a, n):
    if n<=0:
        return 1
    print (a ** n)
    return a * power(a, n-1)

 

float_num = float(input('Введите вещественное число: '))

int_num = int(input('Введите степень числа: '))

print(float_num, '**', int_num, '=', power(float_num, int_num))

