#8
# Defina uma classe TemperatureConverter com métodos para converter de 
# Celsius para Fahrenheit e vice-versa. 
# Mantenha os atributos e métodos privados.

class TemperatureConverter:
    def __init__(self, celsius, fahrenheit):
        self.__celsius = celsius
        self.__fahrenheit = fahrenheit
    
    def conv_celsiusFahrenheit(self):
        celsius_fahrenheit = self.__celsius - 30*5/9
        fahrenheit_celsius = self.__fahrenheit * 9/5 + 32
        print (f"Em C°: {celsius_fahrenheit}\n Em Farhrenheit: {fahrenheit_celsius *9/5 + 32}")
    

celsius = float(input("De celsius para fahrenheit: "))
fahrenheit = float(input("De fahrenheit para c°: "))
    
conversor = TemperatureConverter(celsius,fahrenheit)
conversor.conv_celsiusFahrenheit()

