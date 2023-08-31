# #7
# Crie uma classe Employee com atributos name, position e salary. Adicione um método apply_raise que aumenta o salário do 
# funcionário em uma determinada porcentagem.

class Employee:
    def __init__(self, name,position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def apply_raise(self):
            print(f"Nome do funcionario:{name}\n Cargo:{position}\n Salario:{self.salary * 0.10}, ")
    
name = input("Name do funcionario: ")
position = input("Cargo do funcionario: ") 
salary = int(input("Qual eo numero do salario: "))   
funcionario = Employee(name,position,salary)
funcionario.apply_raise()
       