# -*- coding: cp1251 -*-
import msvcrt


glonbal_count=-1
count=0
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
def all_dicts(a_dict):
    yield a_dict

    for key in a_dict:
      
        if isinstance(a_dict[key], dict):

                yield from all_dicts(a_dict[key])


def lookup(a_dict, key,g_count,count):
    
    for d in all_dicts(a_dict):
        
        if key in d:
         
            return d[key]
        count+=1
        #print('Уровень',count)
        if count==g_count:
             break

my_str=input('Введите искомый ключ:')
print('хотите ввести максимальную глцбину? Y/N')
b=True

    


while b:

         key=msvcrt.getch()
         if key ==b'y':
                    while True:

                     glonbal_count=input('введите глубину :')
                     try:
                         glonbal_count=int(glonbal_count)
                         break

                     except ValueError:
                        print("не Число ") 
                    
                    b=False
         if key==b'n':
             b=False


print(lookup(site,my_str,glonbal_count,count))