# -*- coding: cp1251 -*-

import os


def path_p(nam_f):
	path=os.path.join('9','task1',nam_f)
	file_n_path=os.path.abspath(path).replace('\\','\\\\')
	return file_n_path
file_answer='answer.txt'
file_namber='numbers.txt'

file_namber_path=path_p(file_namber)
print (file_namber_path)
file_answer_path=path_p(file_answer)
print (file_answer_path)

speak_file=open(file_namber_path,'r')

file=speak_file.read()
str_f=[]
for i_el in file:
	
	if i_el and i_el!=' ' and i_el!='\n':
		str_f.append(int(i_el))
		
suma=sum(str_f)

r_file=open(file_answer_path,'+a')
str_suma=str(suma)+' '
if len(str_suma)>10:
	str_suma+='\n'
r_file.write(str_suma)
print(str_suma)
r_file.close()
speak_file.close()