# -*- coding: cp1251 -*-

class Human :
    __age=0
    __name=None
    def __init__(self,name,age):
     self.set__age(age)
     self.set__name(name)

    def __str__ (self):
        return "��� {} ������� {}".format(self.__name,self.__age)

    def set__name(self, name):
        if name.isalpha():
            self.__name=name
            
        else:
            raise Exception("����������� ���")

    def set__age(self, age):
        if age>0 and age<100:
            self.__age=age
            
        else:
            raise Exception("����������� �������")
        


hum_1=Human('����',55)
print(hum_1)

hum_2=Human('RRR',-11)


print(hum_2)