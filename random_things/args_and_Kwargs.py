# in the file "aula20" line 41 have a *arg functionality byt not have the **kwarg, so review and **kwarg

# --------------*args-----------------
# * is passed before the argument, when don't know how many values(uniques) will go passed by the argument
def cont(*num):
    print("The values are: ", end="")
    for c in num:
        print(f" {c}", end="-")
    print(f">  They are in overall {len(num)} numbers", end=".")


cont(1, 2, 3, "fork")


# -------------**kwargs---------------
# ** is pass before de argument, use this to pass values in format of dictionary(key, value)
"""def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print(f"{key} = {value}")


intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)"""
