# -*- coding: cp1251 -*-
import collections


def count_repeats(lst):
    "Возвращает словарь, в котором каждому элементу списка lst соответствует количество его повторений"
    repeats = {}
    for item in lst:
        if item in repeats:
            repeats[item] += 1
        else:
            repeats[item] = 1
    

    return repeats

str=input('input str : ')
vocabulary={}
dict_str={}

for i_str in range (len(str)):
    
    dict_str[str[i_str]]=0
for i in str:
    
    if i in dict_str:
        dict_str[i]+=1



count_repeats(dict_str)
for i_sem in sorted(dict_str.keys()):
        print(i_sem,':', dict_str[i_sem])

for leater,serial_num in collections.Counter(str).items():
    vocabulary.setdefault(serial_num,[]).append(leater)
print('\nИнвертированный словарь частот:')
for i in vocabulary:
    print(i, vocabulary[i])

           