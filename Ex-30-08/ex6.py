#6
# Desenvolva uma classe Book com atributos title, author e year.
# Implemente um método get_age que retorna quantos anos o 
# livro tem desde o ano atual.

class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def get_age(self):
        print(f"author:{self.author} , Titulo:{self.title}, Ano:{ 2023 - self.year}")

author = input("Qual eo nome do livro: ")
title = input("Qual eo nome do author: ")
year = int(input("Data do livro: "))
book  = Book(title,author,year)
book.get_age()
