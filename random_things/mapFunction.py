"""
Resume: the map() have 2 parameters
    The first is a function, to which map passes each element of given iterable.
    The second is a iterable which is to be mapped(list, tuple etc.).

"""

"""
l1 = [1, 2, 3, 4]
l2 = [4, 3, 2, 1]


def func(x):
    return x*x


print(list(map(func, l1)))
print(list(map(func, (1, 2, 5, 6))))
print({map(func, l1)}, "tem esse mesmo resultado para map entre (), {}, []")

"""

"""
#isto n funciona pois o map so serve para listas unicas de valoeres
print(list(map(func, l1, l2)))
or
print(list(map(func, (l1, l2))))
"""

"""
def soma(x):
    return x + 1
    

print(list(map(soma, map(func, l1))))
"""

"""
li = [1, 2, 3, 4, 5]
print(list((map(lambda x: x * 2, map(lambda x: x * 4, map(lambda x: x * 8, li))))))

"""

"""
dic = {"mes": 6,
       "ano": 2010,
       "dia": 20
       }

a = list(map(lambda x: x, dic.keys()))
b = list(map(lambda x: x, dic.values()))

for p, s in enumerate(b):
    print(f"{a[p]} --- {b[p]}")
"""
