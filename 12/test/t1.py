# -*- coding: cp1251 -*-


from logging import raiseExceptions
from re import X


class Koordinaty:
   
    def __init__(self, x,y):
        self.set_x(x)
        self.set_y(y)
    def __str__(self):
        return " X: {} Y: {} ".format(self.x,self.y)
    def set_x(self,nam):
        
            if isinstance(nam, int):
                self.x=nam
                
                return
            else:
                raise Exception ("это не число")
    def set_y(self,nam):
        if isinstance(nam, int):
                self.y=nam
                
                return
        else:
                raise  ("это не число")
try:
    X=Koordinaty(10,11)
except NameError:
    print(' Name Error !!!')
print(X)
