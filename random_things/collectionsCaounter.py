from collections import Counter

a = Counter("gallad")
print(a, a["a"])
print("\n")

b = Counter(["a", "a", "b", "c", "c"])
print(b)
print(b.most_common(1))
# the number defined how many elements you want show, without elements print all of them
print("\n")

c = Counter({"a": 1, "b": 2})
print(c, c["f"])
# c in a position not fond return 0, but if did a dictionary on python would give error
print("\n")

d = Counter(cats=4, dogs=7)
print(d)
print(list(d.elements()))
print(d.most_common(1))
print("---------------------------------------")
# this subtract e(elements) - c(elements)
e = Counter(a=4, b=2, c=0, d=-2)
f = ["a", "b", "b", "c"]
e.subtract(f)
print(e)
e.update(f)
print(e)
#print(e.clear())

print("---------------------------------------")
g = Counter(a=4, b=2, c=0, d=-2)
h = Counter(["a", "b", "b", "c"])
# don't show numbers <= 0
print(g+h)
print(g-h)
print("\n")
# intersection is the minimum element in each(don't show <= 0)
print(g & h)
print("\n")
# union is the maximum element in each(don't show <= 0)
print(g | h)
