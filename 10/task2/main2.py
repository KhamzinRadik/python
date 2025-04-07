# -*- coding: cp1251 -*-


from path_file import path_p
import os
import random

dirrectory=['10','task2']
extract_zip=path_p(dirrectory)
file_text=path_p(dirrectory,'out_file.txt')

while(True):
    summ=0
    with open(file_text, 'a') as f_namlist:
            nam=int(input('введите число: '))
            f_namlist.write(str(nam)+' ')

    with open(file_text, 'r') as f_namlist:
        str_list=''
        for i in f_namlist:
            str_list+=i
    str_list=str_list.split()
    for i in range ( len(str_list)):
        
       summ+=int(str_list[i])
    if summ>=777:
        break
    print(summ)
    x = random.randint(1, 13)
    try:
        if x == 7:
            raise ValueError ("unlucky")
           
            
    except:
        print("unlucky")
            
        break