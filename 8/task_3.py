# -*- coding: cp1251 -*-
import copy
import pprint 


site = {
    'html': 
    {
        'head': 
        {
            'title': '�����/������ ������� ��������'
        },
        'body': 
        {
            'h2': '� ��� ����� ������ ���� �� �������',
            'div': '������',
            'p': '�������'
        }
    }
}

my_str=int(input('������� ������:'))
new_sait=copy.deepcopy(site)

for i in range (my_str):

    new_produckt=input('������� �������� �������� ��� ������ �����: ')
    
    new_sait[new_produckt]=copy.deepcopy(site)
    new_sait[new_produckt]['html']['head']['title']=f'�����/������ {new_produckt} ��������'
    new_sait[new_produckt]['html']['body']['h2']=f'� ��� ����� ������ ���� �� {new_produckt}'

    pprint.pprint(new_sait[new_produckt])
    


