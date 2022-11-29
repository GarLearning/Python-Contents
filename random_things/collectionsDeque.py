from collections import deque

# use a deque
d = deque("hello")
print(d)
# append values in a deque(on the end deque and in start)
d.append("4")
d.appendleft(5)
print(d)
# pop(remove) values in a deque(on the end deque and in start)
d.pop()
d.popleft()
print(d)
# remove everything from a deque
d.clear()
print(d)
# this method, extend, take anything from a container() and put at the and of a list
# the extend doesn't put a iterable values, but put a list with values iterable
d.extend("123")
print(d)
d.extend("hello")
print(d)
d.extend([1, 2, 3])
print(d)
d.extend(["123"])
print(d)
d.extend([[123]])
print(d)
d.extendleft("hey")  # append in the left in a reverse order(because extending h after e after y staying yeh)
print(d)
# from positive integer in a rotate all of the values is amount to the right and negative to the left
d.rotate(-3)  # -3 did hey(yeh) what have 3 characters put in the final deque(list)
print(d)
d.rotate(4)  # put hey(3) and [123] in the beginning of the deque
print(d)
print("---------------------")
c = deque("hello", maxlen=5)  # remove de first element if put another there
print(c)
c.append(1)
print(c)
