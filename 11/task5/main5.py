# -*- coding: cp1251 -*-


import random 


class Human: 
    def __init__(self, name, satiety=50): 
        self.name = name 
        self.satiety = satiety 

    def eat(self): 
        self.satiety += 10 
        print(f'{self.name} ����. �������: {self.satiety}') 

    def work(self): 
        self.satiety -= 10 
        print(f'{self.name} ���������. �������: {self.satiety}') 

    def play(self): 
        self.satiety -= 10 
        print(f'{self.name} �������. �������: {self.satiety}') 


class House: 
    def __init__(self, food=50, money=0): 
        self.food = food 
        self.money = money 

    def buy_food(self): 
        self.food += 10 
        self.money -= 10 
        print('������� ���') 

    def earn_money(self): 
        self.money += 10 
        print('���������� ������') 


human1 = Human('������') 
human2 = Human('�����') 
house = House() 

for day in range(1, 366): 
    print(f'\n���� {day}:') 
    number1 = random.randint(1, 6) 
    number2 = random.randint(1, 6) 

    if human1.satiety < 20: 
        human1.eat() 
    elif house.food < 10: 
        house.buy_food() 
    elif house.money < 50: 
        house.earn_money() 
    elif number1 == 1: 
        human1.work() 
    elif number1 == 2: 
        human1.eat() 
    else: 
        human1.play() 

    if human2.satiety < 20: 
        human2.eat() 
    elif house.food < 10: 
        house.buy_food() 
    elif house.money < 50: 
        house.earn_money() 
    elif number2 == 1: 
        human2.work() 
    elif number2 == 2: 
        human2.eat() 
    else: 
        human2.play() 

    if human1.satiety <= 0 and human2.satiety <= 0: 
        print('��� ������ �� ������.') 
        break 
    elif human1.satiety <= 0: 
        print(f'{human1.name} ���� �� ������.') 
        break 
    elif human2.satiety <= 0: 
        print(f'{human2.name} ���� �� ������.') 
        break
