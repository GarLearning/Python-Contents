"""
Have a use similar to map, but your use is for returns TRUE or FALSE.
"""

"""
l1 = [1, 2, 3, 4]
l2 = [4, 3, 2, 1]


def soma(x):
    return x + 1


def func(x):
    return x*x


m = list(filter(func, l1))
print(list(map(soma, filter(func, l1))))
"""


"""
l1 = [0, 1, 2, 0, 3, 4]

# print(list(filter(lambda x: (x + 1) % 2, l1)))
a = lambda x: (x + 1) % 2
print(list(filter(a, l1)))
"""

lis = [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
listes = ["sas", "asa", "", "dss"]
a = list(filter(None, listes))
b = lambda x: 6 / x
for t in a:
    print(t)
