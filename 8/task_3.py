# -*- coding: cp1251 -*-
import copy
import pprint 


site = {
    'html': 
    {
        'head': 
        {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': 
        {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

my_str=int(input('Сколько сайтов:'))
new_sait=copy.deepcopy(site)

for i in range (my_str):

    new_produckt=input('Введите название продукта для нового сайта: ')
    
    new_sait[new_produckt]=copy.deepcopy(site)
    new_sait[new_produckt]['html']['head']['title']=f'Куплю/продам {new_produckt} недорого'
    new_sait[new_produckt]['html']['body']['h2']=f'У нас самая низкая цена на {new_produckt}'

    pprint.pprint(new_sait[new_produckt])
    


