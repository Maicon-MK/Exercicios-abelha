
#5Defina uma classe Car com atributos make, model e year. 
#Crie um método start_engine que imprime uma mensagem
#indicando que o motor foi iniciado.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def ligar(self):
        print("On")
    def desligar(self):
        print("Off")
    def especificacoes(self):
        print(self.make,self.model,self.year)

uno = Car('Black', 'rapido', '2016')
uno.ligar()
uno.especificacoes()
uno.desligar