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
print(len(name_mail_age))

# for i in range (len(name_mail_age)):
#     print('I :',i ,'\n\t')
i=1
for i_el in name_mail_age:
         print('\ti_el',i_el.split())
         try:
             if len(name_mail_age[i])<3:
            
                     raise (i,'не полная информация')
         except:
             print (i,'не полная информация')
             count+=1
         try:
            if not i_el.isalpha():        
                raise (i,'имя содержит не только буквы')
         except:
             print(i,'имя содержит не только буквы')
             count+=1
        # try:
        #     if not '@' in name_mail_age[1]:
        #         raise ('не корректная почта')      
        # except:
        #     print('не корректная почта')   
        #     count+=1
        
        # try:
        #     if name_mail_age[2].isdigit():
        #         age=int(name_mail_age[2])
        #     else:
        #             print('не корректный возраст')
        # except:
        #     print('не корректный возраст') 
        #     count+=1
        # try:
        #     if (age<10 or age >99):
        #         raise ('не корректный возраст')
        # except:
        #     print('не корректный возраст')
        #     count+=1
        # if count<1:
        #     name_mail_age_str=''
        #     for i in name_mail_age:
        #         name_mail_age_str+=i+' '
        #     print (name_mail_age_str)
        #     with open(file_text, 'a') as f_namlist:
        #         f_namlist.write(name_mail_age_str)

         i+=1