#com isso da para criar um erro com base em uma condicional "a > 5", e tratar como except, ja q except so trata de erros padroes.
#quando o assert é assionado ele para o programa, a menos q esteja com algum tipo de tratamento(loop, try/except)
"""a = 4
try:
    assert a > 5
    print(a)
except AssertionError:
    print("this value is small 5")"""

#erros encadeados, o comando int(num) deu erro pq o result da variavel num era uma divisão por 0 q é outro erro
"""try:
    num = 1/0
    int(num)
except Exception as e:
    raise ValueError from e
"""

while True:
    try:
        num = int(input("Enter a whole number between 1 and 20: "))
        num1 = int(num)
    except ValueError:
        print("Type just whole number!")
    except:
        print("Invalid input! try again.")
    else:
        break

test = True
if not 1 <= num <= 20:
    test = False

if __debug__:
    if not test:
        raise AssertionError(num1)

print(num)
#esse metodo de debug é semelhante ao assert a baixo

"""assert 1 <= num <= 20, "This number not in 1 and 20."#mensagem apos o assert erro"""




#ESTUDAR A PARTE DE DBUG DE UM PROGRAMA COM ASSERT E SUAS FUNCIONALIDADES
