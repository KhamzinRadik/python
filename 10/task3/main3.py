# -*- coding: cp1251 -*-



from turtle import reset
from xml.dom.minidom import Element
from path_file import path_p
import os
import random


dirrectory=['10','task3']
extract_zip=path_p(dirrectory)
file_text=path_p(dirrectory,'registrations.txt')
name_mail_age=[]
bad_log=[]
good_log=[]

with open(file_text, 'r') as f_namlist:
    for i in f_namlist:
        name_mail_age.append(i.rstrip())
i=0
error=[]
for i_el in name_mail_age:
    i_element=i_el.split()
    
    try:
        if len(i_element)<3:
            error.append(': не полная информация о пользователе! ')
            raise ValueError (i_element+error)

        if not i_element[0].isalpha(): 
            error.append(': Поле «Имя» не корректно! ')
            raise ValueError (i_element+error)
        if (not '@' in i_element[1] or not '.' in i_element[1]):
                    error.append( ': Поле «Маил» должно содержать "." и "@" ! ')
                    raise ValueError (i_element+error)
        if len(i_element[1])<3:
                    error.append( ': Поле «Маил» НЕ корректно! ')
                    raise ValueError (i_element+error)
        if i_element[2].isdigit():
                    age=int(i_element[2])
        else:
                    
                    error.append( ': Поле «Возраст» НЕ представляет число от 10 до 99! ')
                    raise ValueError (i_element+error)
        if (age<10 or age >99):
                    error.append( ': Поле «Возраст» не соответствует критериям от 10 до 99! ')
                    raise ValueError (i_element+error)
    except(ValueError) as exc:
        print(str(exc))
        er_str=' '.join(i_element+error)
       
        bad_log.append(er_str)


    else:
         good_log.append(i_element)
    error.clear()
name_mail_age.clear()

  

file_text_b_l=path_p(dirrectory,'bad.log')          
with open(file_text_b_l, 'w',encoding='utf-8') as f_namlist:
    i=0
    while bad_log:
        f_namlist.write(str(bad_log.pop())+'\n')
        i+=1
          
file_text_b_l=path_p(dirrectory,'good.log')
with open(file_text_b_l, 'w') as f_namlist:
    i=0
    while good_log:
        f_namlist.write(str(good_log.pop())+'\n')
        i+=1


         