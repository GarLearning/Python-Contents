from collections import namedtuple
# two parameters, fist refer to variable than will be treated, and the second will be values
# than will be separated
point = namedtuple("point", "x y z")
# quantity values and your positions
newP = point(3, 4, 5)
print(newP)
print("\n")

# this works to list, tuples and dictionary(show de key values)
point2 = namedtuple("point2", ["x", "y", "z", "h"])
newP2 = point2(1, 2, -3, 10)
print(newP2)
print(newP2.h, newP2.z, newP2.y, newP2.h, newP2.x)
print(newP2[1], newP2[3], newP2[0], newP2[2])
print(newP2._asdict())
print(newP2._fields)
print(newP2._replace(x=10))
# remake a list of values to namedtuple
p2 = point2._make(["a", "b", "c", 4])
print(p2)
print("\n")

point3 = namedtuple("point3", {"x": 1, "y": 2})
newP3 = point3(1, 2)
print(newP3)

print(newP3._replace(x=4))
