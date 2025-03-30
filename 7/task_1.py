# -*- coding: cp1251 -*-

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def fun(dict):
     id_age={}
     interests_=[]
     len_surename = ''
     for i_key, i_value in students.items():
         id_age[i_key]=i_value['age']
         interests_ += (dict[i_key]['interests'])
         len_surename += dict[i_key]['surname']
        
     return id_age,interests_, len_surename

my_lst = fun(students)


print('Список пар «ID студента — возраст»:\n\t\t\t\t', my_lst[0],
      '\nПолный список интересов всех студентов:\n\t\t\t\t',my_lst[1],
      '\nОбщая длина всех фамилий студентов:\n\t\t\t\t',len( my_lst[2]))