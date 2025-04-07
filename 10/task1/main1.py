# -*- coding: cp1251 -*-


from path_file import path_p
import os

dirrectory=['10','task1']
extract_zip=path_p(dirrectory)
file_text=path_p(dirrectory,'people.txt')
print(file_text)
nam=''
line_count=0
try:
    simvol=0
    with open(file_text, 'r') as str_text:
        for i_el in str_text:
         nam+=i_el
    
    str_text=nam.split()

    for i in str_text:
        length = len(i)
        simvol+=len(i)
        line_count += 1

        try:
           if len(i)<3:
               raise ValueError('Ошибка: менее трёх символов в строке:', line_count)
        except ValueError:
               print('Ошибка: менее трёх символов в строке:', line_count)
except FileNotFoundError:
    print('фаил не найден')

    

finally:
    print('Общее количество символов:',simvol)
