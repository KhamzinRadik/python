# -*- coding: cp1251 -*-
import msvcrt


glonbal_count=-1
count=0
site = {
    'html': {
        'head': {
            'title': '��� ����'
        },
        'body': {
            'h2': '����� ����� ��� ���������',
            'div': '���, ��������, �����-�� ����',
            'p': '� ��� ����� ����� �����'
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
        #print('�������',count)
        if count==g_count:
             break

my_str=input('������� ������� ����:')
print('������ ������ ������������ �������? Y/N')
b=True

    


while b:

         key=msvcrt.getch()
         if key ==b'y':
                    while True:

                     glonbal_count=input('������� ������� :')
                     try:
                         glonbal_count=int(glonbal_count)
                         break

                     except ValueError:
                        print("�� ����� ") 
                    
                    b=False
         if key==b'n':
             b=False


print(lookup(site,my_str,glonbal_count,count))