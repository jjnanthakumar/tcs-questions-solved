# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"

from collections import OrderedDict
class Student:
    def __init__(self, RollNo, Name, Class, percentage):
        self.rollno = RollNo
        self.name = Name
        self.class_=Class
        self.percentage = float(percentage)
        self.grade = None
        
class School:
    def __init__(self, studentObj):
        self.student_obj = studentObj
    
    @staticmethod
    def grade(x):
        if x in range(75,100+1):
            return 'A'
        elif x in range(60,74+1):
            return 'B'
        elif x in range(40,59+1):
            return 'C'
        elif x in range(30,39+1):
            return 'D'
        else:
            return 'E'

    def calculate_grade(self):
        for ele in self.student_obj:
            ele.grade = self.grade(ele.percentage)
        out = OrderedDict({'A':0,'B':0,'C':0,'D':0,'E':0})
        for ele in self.student_obj:
            out[ele.grade]=out.get(ele.grade,0)+1
        return out
    
    def get_students_by_percent(self, percent):
        filtered = list(filter(lambda x:x.percentage>=percent,self.student_obj))
        return sorted(filtered,key=lambda x: x.percentage,reverse=True) if filtered else None

n = int(input())
student_objects = []
for _ in range(n):
    student_objects.append(Student(int(input()),input(),int(input()),int(input())))

school = School(student_objects)
percent = int(input())
out = school.calculate_grade()
print('\n'.join(f'{k} : {v}' for k,v in out.items()))

get = school.get_students_by_percent(percent)
if get is None:
    print("No student scored more that the cutoff percentage")
else:
    for ele in get:
        print(ele.rollno,ele.name,ele.class_,round(ele.percentage,1))