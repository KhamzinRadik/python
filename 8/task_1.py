# -*- coding: cp1251 -*-
def rek(nam,nam2):
   
    
    if nam2 != nam:
        print(nam2)
        return rek(nam,nam2+1)
    else:
        return 0



nam=int(input('Введите num :'))
nam2=nam
rek(nam,nam2-nam+1)