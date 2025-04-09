# -*- coding: cp1251 -*-



from path_file import path_p
import os
import random


dirrectory=['10','task3']
extract_zip=path_p(dirrectory)
file_text=path_p(dirrectory,'registrations.txt')
name_mail_age=[]

with open(file_text, 'r') as f_namlist:
          for i in f_namlist:
              name_mail_age.append(i.rstrip())

        
count=0
i=0


dirrectory=['10','task3']
file_text_b_l=path_p(dirrectory,'bad.log')
         
            
with open(file_text_b_l, 'w') as f_namlist:
    for i_el in name_mail_age:
             count=0
            
             bad_log=[]
             good_log=[]
             elstr=i_el.split()
             
             try:
                  
                  if len(elstr)<=2:
                     
                   raise 
             except:
                  print (i,'не полная информация')
                  count+=1
             try:
            
                if not elstr[0].isalpha(): 
                    
                    raise 
             except:
                 print(i,elstr[0],'имя содержит не только буквы')
                 count+=1
         
             try:
                if (not '@' in elstr[1] or not '.' in elstr[1]):
                    raise
                if len(elstr[1])<3:
                    raise
                    count+=1
             except:
                print('не корректная почта1111',elstr)   
                count+=1
        
             try:
                if elstr[2].isdigit():
                    age=int(elstr[2])
                else:
                    raise
                    count+=1
                if (age<10 or age >99):
                    
                    raise
                    count+=1
             except:
                print('не корректный возраст')
                count+=1
             
             
             if count >= 1:
                            
                  f_namlist.write(name_mail_age[i]+'\n')
                  print('dellite ',name_mail_age.pop(i))
                  i-=1
              
             i+=1
            
file_text_b_l=path_p(dirrectory,'good.log')
with open(file_text_b_l, 'w') as f_namlist:
                for i_el in  name_mail_age:
                    f_namlist.write(i_el+'\n')

         