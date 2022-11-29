from POO_python.pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

p1.falar("eae")
p2.falar("como vai")
p1.comer("Arroz")
p2.parar_falar()
p2.falar("qual a sua idade?")
p1.parar_falar()
p1.falar(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
