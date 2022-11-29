class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
            self.nome = nome
            self.idade = idade
            self.comendo = comendo
            self.falando = falando

            variavel = "valor"

    def outro_metodo(self):
            print(variavel)#n tem o self, na de cima fazendo com q n seja de scopo da classe inteira, mais se colocado o self ela nuncionaria
            print(self.nome)#esse tem self
#tirar o self do parametro daria confusão de p1 com p2 30min video1(ficariam dependentes)