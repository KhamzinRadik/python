# -*- coding: cp1251 -*-



from path_file import path_p
import os



dirrectory=['10','task3']
extract_zip=path_p(dirrectory)
file_text=path_p(dirrectory,'registrations.txt')
name_mail_age=[]

with open(file_text, 'r') as f_namlist:
          for i in f_namlist:
              name_mail_age.append(i.rstrip())

for i in name_mail_age.split():
    
    #print (i)
    
   # print(i.split())
   
   print(i)
   # if len(SS[2])<3:
   #   print (SS)