l1 = [1, 2, 3, 4, 1]

print("True" if len(l1) % 2 == 0 else "False")
print([x for x in l1])
print([x for x in l1 if x % 2 == 0])
print((x for x in l1 if x % 2 == 0))
print({x for x in l1 if x % 2 == 0})
#y = 0
#print([y while y < 5 y += 1])
#print("True" if len(l1) % 2 == 0 "Maybe"elif len(l1) % 2 == 1 else "False")

grade = [73, 67, 38, 33]


def grades(g):
    return [n if n < 38 or n % 5 < 3 else (n + 5 - (n % 5)) for n in g]


r = grades(grade)
print(r)
