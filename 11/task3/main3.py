# -*- coding: cp1251 -*-

from random import choice 


class Parent: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
        self.lst_childs = [] 

    def add_child(self, child): 
        if self.age - child.child_age > 16: 
            self.lst_childs.append(child) 
            print(f'{child.name} добавлен в семью.') 
        else: 
            print(f'{child.name} ты не ребенок {self.name}.') 

    def info_parent(self): 
        print(f'{self.name} {self.age} лет') 
        for child in self.lst_childs: 
            print(f'{child.name} {child.child_age} лет {child.state_calm} и {child.state_hunger}') 

    def calm_down(self): 
        for child in self.lst_childs: 
            if 'балуется' in child.state_calm: 
                print(f'{child.name} {child.state_calm}, успокоим.') 
                child.state_calm = 'спокоен' 

    def hunger(self): 
        for child in self.lst_childs: 
            if 'голоден' in child.state_hunger: 
                print(f'{child.name} {child.state_hunger}, накормим.') 
                child.state_hunger = 'сыт' 


class Children: 
    state_calm = ['балуется', 'спокоен'] 
    state_hunger = ['голоден', 'сыт'] 

    def __init__(self, name, child_age): 
        self.name = name 
        self.child_age = child_age 
        self.state_calm = choice(Children.state_calm) 
        self.state_hunger = choice(Children.state_hunger) 


parent = Parent('Сильвестр Андреевич', 45) 
child_1 = Children('Таня', 20) 
child_2 = Children('Саша', 25) 

parent.add_child(child_1) 
parent.add_child(child_2) 

parent.calm_down() 
parent.hunger() 
parent.info_parent()