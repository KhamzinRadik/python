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
            print(f'{child.name} �������� � �����.') 
        else: 
            print(f'{child.name} �� �� ������� {self.name}.') 

    def info_parent(self): 
        print(f'{self.name} {self.age} ���') 
        for child in self.lst_childs: 
            print(f'{child.name} {child.child_age} ��� {child.state_calm} � {child.state_hunger}') 

    def calm_down(self): 
        for child in self.lst_childs: 
            if '��������' in child.state_calm: 
                print(f'{child.name} {child.state_calm}, ��������.') 
                child.state_calm = '�������' 

    def hunger(self): 
        for child in self.lst_childs: 
            if '�������' in child.state_hunger: 
                print(f'{child.name} {child.state_hunger}, ��������.') 
                child.state_hunger = '���' 


class Children: 
    state_calm = ['��������', '�������'] 
    state_hunger = ['�������', '���'] 

    def __init__(self, name, child_age): 
        self.name = name 
        self.child_age = child_age 
        self.state_calm = choice(Children.state_calm) 
        self.state_hunger = choice(Children.state_hunger) 


parent = Parent('��������� ���������', 45) 
child_1 = Children('����', 20) 
child_2 = Children('����', 25) 

parent.add_child(child_1) 
parent.add_child(child_2) 

parent.calm_down() 
parent.hunger() 
parent.info_parent()