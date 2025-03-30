# -*- coding: cp1251 -*-
import msvcrt
import os



def add_contackt(contackt_l):

     print("Введите имя и фамилию нового контакта (через пробел): ")
     while True:

         str_name= input().split()
         name=(str_name[0], str_name[1])
     

         if name in contackt_l:
              
              print('Такой человек уже есть в контактах.')
         else:
          
              phone_namber=int(input('Введите номер телефона: '))
              contackt_l[name]=phone_namber
              
         print('для выхода нажмите Esc ')
         key=msvcrt.getch()
         if key==b'\x1b':
             break
     return contackt_l
def poisk (contackt_list):
    shared_name={}
    print (contackt_list)
    f_l_name= input("Введите фамилию для поиска: ").lower()
    for i in contackt_list:
        if f_l_name == i[1] or f_l_name==i[0] :
            clear()
            print(*i,'номер телефона :',contackt_list[i])
        else:
            clear()
            print('Такой уонтакт не найден')




contackt_list={}

while True:
        clear = lambda: os.system('cls')
        
        print('\t\t\t\tВведите номер действия:\n\t\t\t\t',
              '1 Добавить контакт.\n\t\t\t\t',
              '2 Найти человека.\n\t\t\t\t',
              '3 Выход\n\t\t\t\t ')
    
        key=msvcrt.getch()
        

        if (key == b'1'):
            add_contackt(contackt_list)   
            
        if (key == b'2'):
            poisk(contackt_list)
            
               
                
        
   

