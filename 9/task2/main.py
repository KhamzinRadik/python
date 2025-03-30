# -*- coding: cp1251 -*-

import os
def path_p(nam_f):
	path=os.path.join('9','task2',nam_f)
	file_n_path=os.path.abspath(path).replace('\\','\\\\')
	return file_n_path
file_name='zen.txt'

file_name_path=path_p(file_name)
speak_file=open(file_name_path,'r')
file=speak_file.readlines()

for i_str in range (len(file)-1,0,-1):

	
     print(file[i_str])