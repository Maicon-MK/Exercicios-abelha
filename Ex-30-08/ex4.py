
#4Crie uma classe Student com atributos name, age e grades (uma lista).
#Adicione métodos para adicionar notas,
#calcular a média das notas e exibir as informações do aluno.

class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.grades = []

    def __str__(self):
        return f"Name: {self.name}\n Age: {self.age}"
    
    # @property
    # def name(self):
    #     self.__name 
    
    # @name.setter
    # def name(self,name):
    #     self.__name = name
    
    def add_grade(self,grade):
        self.grades.append(grade)
    
    def soma(self):
        total = sum(self.grades)
        media = total / len(self.grades)
        return media
    def info (self):
        print(
              f"Name: {self.name}\n Age: {self.age}\n Grades: {self.grades} \n Media: {self.soma()}")

name_student = input("Name student: ")
age_student = int(input("Age student: "))
estudant = Student(name_student,age_student)

for i in range(4):
    grade = float(input(f"Value nota {i+1}: "))
    estudant.add_grade(grade)
estudant.info()