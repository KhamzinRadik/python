import os

from path_file import path_p






dirrectory=['9','task5']
file_text=path_p(dirrectory,'text.txt')
file_analysis=path_p(dirrectory,'analysis.txt')
text=''
working_file=open(file_text,'r')
for i_el in working_file:
    text+=i_el
working_file.close()

count_bukva=0
text=text.replace(' ','').lower()
size_str=len(text)
print(size_str)
text_d={}
for i in text:
    text_d[i]=0
    print (i)
for i in (text_d):
    count=0
    for y in range (len(text)):
        if i==text[y]:
            count+=1
    fl=round(float(count/size_str),3)

    text_d[i]=fl
    print(i)
working_file=open(file_analysis,'r+')
for key,value in text_d.items():
    k=str(key)
    v=str(value)
    text=k+': '+v
    print('key',k,'value',value)
    
    print('text',text)
    working_file.write(text+'\n')
working_file.close()
print(text_d)
