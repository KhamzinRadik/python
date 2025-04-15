# -*- coding: cp1251 -*-

from random import randint 


class Students: 
    def __init__(self, name, group, grade): 
        self.name = name 
        self.group = group 
        self.grade = grade 

    def average_score(self): 
        return sum(self.grade) / len(self.grade) 

    def info_student(self): 
        print(self.name, self.group, self.grade, self.average_score()) 


out_student = [ 
    ['Студент 1', '2А', [randint(2, 5) for _ in range(5)]], 
    ['Студент 2', '2Б', [randint(2, 5) for _ in range(5)]], 
    ['Студент 3', '3А', [randint(2, 5) for _ in range(5)]], 
    ['Студент 4', '3А', [randint(2, 5) for _ in range(5)]], 
    ['Студент 5', '3Б', [randint(2, 5) for _ in range(5)]], 
    ['Студент 6', '3Т', [randint(2, 5) for _ in range(5)]], 
    ['Студент 7', '5А', [randint(2, 5) for _ in range(5)]], 
    ['Студент 8', '3Б', [randint(2, 5) for _ in range(5)]], 
    ['Студент 9', '3Г', [randint(2, 5) for _ in range(5)]], 
    ['Студент 10', '3А', [randint(2, 5) for _ in range(5)]] 
   ] 

lst_student = [] 

for i in range(len(out_student)): 
    lst_student.append(Students(out_student[i][0], out_student[i][1], out_student[i][2])) 

sort_students = sorted(lst_student, key=lambda item: item.average_score()) 

for student in sort_students: 
    student.info_student()