# -*- coding: cp1251 -*-
str=input("Введите текст:")

list=['а','е','ё','и','й','о','у','э','ю','я']

list_glasnie =[i for i in str if i in list]

print("Список гласных букв:",list_glasnie)
print("Длина списка:",len(list_glasnie) )


