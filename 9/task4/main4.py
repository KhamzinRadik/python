# -*- coding: cp1251 -*-
import os

from path_file import path_p



#D:\gitClone\KhamzinRadik\python-2.5\9\task4\main.py


dirrectory=['9','task4']
file_path_first=path_p(dirrectory,'first_tour.txt')
file_path_second=path_p(dirrectory,'second_tour.txt')


students=[]
new_students=[]
working_file=open(file_path_first,'r')
for i_el in working_file:
    students.append(i_el)
k=int(students.pop(0))
working_file.close()
while students:
    new_students.append(students.pop())
working_file=open(file_path_second, 'r+')
working_file.write('Прошли во II тур !\n')
for i_el in new_students:
   
    strf=i_el.split()
    print(strf)
    if int(strf[2])>k:
        nam_f=''
        for i in (strf[1]):
            nam_f=i[0]
            break
        print('nam_f',nam_f)
        strf[1]= str(nam_f.upper())
        
        string=' '.join(strf)
        
        print('string',string.title())
        working_file.write(string+'\n')
        

    

