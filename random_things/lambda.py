# A lambda function can take any number of arguments, but can only have one expression.
# organisation of lambda is, lambda Parameters : Operation
"""
# just use a lambda how a sort function
short_func = lambda x: x * 7
print(short_func(7))
"""


"""
# using lambda with more of one arguments and optional parameters
more_of_one_argument = lambda x, y=2: x + y
print(more_of_one_argument(5, 5))
print(more_of_one_argument(15))
"""


"""
# this print take labbda and pass 5, with print, after multiplies per by the result of the func
def func(y):
    return y - 2


ex1 = lambda x: x * func(4)
print(ex1(5))
"""


"""
#func receive 3 and pass for two lambda after plus them
def func(x):
    func_alternative0 = lambda y: y + 5
    func_alternative1 = lambda z: z - 5
    return func_alternative0(x) + func_alternative1(x)


print(func(3))
"""

"""
# after call func, with func_parameter_2 or func_parameter_3, would be like the value of variable
# were -> lambda y: y * x (x being 2 and 3 from each variable respectively), 
# and in the print pass the value of y of the lambda 
def func(x):
    return lambda y: y * x


# call func
func_parameter_2 = func(2)
func_parameter_3 = func(3)

# call lambda
print(func_parameter_2(2))
print(func_parameter_3(3))

"""

"""
# using lambda with map or filter
# map = entire value(logic of expression) | filter = boolean value(true or false)
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_plus_map = list(map(lambda x: x + 10, l1))
result_pair_filter = list(filter(lambda x: x % 2 == 0, l1))

print(result_plus_map)
print(result_pair_filter)
"""
