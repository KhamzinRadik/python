# -*- coding: cp1251 -*-
import random
class Unit():
	def __init__(self,name):
		self.name=name
		self.hil=100
		self.punch=20
	def print_unit(self):
		print(self.name,'здоровье :',self.hil, 'сила удара :',self.punch)
	

unit1=Unit('Tom')
unit2=Unit('Bill')
while True :
	unit1.print_unit()
	unit2.print_unit()
	if unit1.hil<=0 :
		print(unit2.name, "победил!!!")
		break
	if unit2.hil<=0:
		print(unit1.name, "победил!!!")
		break
	punch_rand=random.randint(1,2)
	if punch_rand==1:
		print(unit2.name,' бьет ', unit1.name)
		unit1.hil=unit1.hil-unit2.punch
	else:
		print(unit1.name,' бьет ', unit2.name)
		unit2.hil=unit2.hil-unit1.punch
	
