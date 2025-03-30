import os
from unittest.util import sorted_list_difference
from collections import OrderedDict

from path_file import path_p
from zipfile import ZipFile 





dirrectory=['9','task6']
extract_zip=path_p(dirrectory)
file_text=path_p(dirrectory,'voina_i_mir.zip')
print(file_text)

with ZipFile(file_text, 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall(extract_zip) 
    print('Done!') 
file_text=path_p(dirrectory,'voina_i_mir.txt')
text=''
working_file=open(file_text,'r')
for i_el in working_file:
    text+=i_el
working_file.close()
text=text.split()
text=''.join(text)
count_bukva=0

size_str=len(text)

text_d={}
for i in text:
    text_d[i]=0
    
for i in (text_d):
    count=0
    for y in range (len(text)):
        if i==text[y]:
            count+=1
    fl=count

    text_d[i]=fl
new_di={}
for key,value in text_d.items():
    new_di[value]=key
    k=str(key)
    v=str(value)
    text=k+': '+v
    #print(k,': ',value)

for key,value in sorted(new_di.items()):
   
    k=str(key)
    v=str(value)
    text=k+': '+v
    print(v,': ',k)  
  
  


