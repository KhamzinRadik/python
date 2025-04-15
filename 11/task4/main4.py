# -*- coding: cp1251 -*-

class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Vapor()
        if isinstance(other, Earth):
            return Dirt()



class Air:

    def __str__(self) :
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return  Storm()

        elif isinstance(other, Fire):
            return Vapor()

        elif isinstance(other, Earth):
            return Dust()
        else:
            return None

class Fire:
    def __str__(self) :
        return 'Огноь'
    def __add__(self, other):
        if isinstance(other, Earth):
            return  Lava()

class Earth:
    def __str__(self) :
        return 'Земля'
    def __add__(self, other):
        if isinstance(other, Fire):
            return  Lava()
        elif isinstance(other, Air):
            return Dust()

class  Storm():
    def __str__(self) :
        return 'Шторм'


class Vapor():
    def __str__(self) :
        return 'Пар'


class Dirt():
    def __str__(self) :
        return 'Грязь'

class Dust():
     def __str__(self) :
        return 'Пыль'

class Lava ():
    def __str__(self) :
        return 'Лава'

water = Water()

air = Air()

fire = Fire()

earth = Earth()

print(air + water, water + fire, water + earth, earth+air)