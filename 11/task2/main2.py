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
    ['������� 1', '2�', [randint(2, 5) for _ in range(5)]], 
    ['������� 2', '2�', [randint(2, 5) for _ in range(5)]], 
    ['������� 3', '3�', [randint(2, 5) for _ in range(5)]], 
    ['������� 4', '3�', [randint(2, 5) for _ in range(5)]], 
    ['������� 5', '3�', [randint(2, 5) for _ in range(5)]], 
    ['������� 6', '3�', [randint(2, 5) for _ in range(5)]], 
    ['������� 7', '5�', [randint(2, 5) for _ in range(5)]], 
    ['������� 8', '3�', [randint(2, 5) for _ in range(5)]], 
    ['������� 9', '3�', [randint(2, 5) for _ in range(5)]], 
    ['������� 10', '3�', [randint(2, 5) for _ in range(5)]] 
   ] 

lst_student = [] 

for i in range(len(out_student)): 
    lst_student.append(Students(out_student[i][0], out_student[i][1], out_student[i][2])) 

sort_students = sorted(lst_student, key=lambda item: item.average_score()) 

for student in sort_students: 
    student.info_student()