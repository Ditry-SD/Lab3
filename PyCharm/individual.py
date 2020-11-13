print("Linear equation solution: ax+b=0")
a = float(input("Type coefficient a = "))
b = float(input("Type coefficient b =  "))
if (a == 0 and b == 0):
    print("An infinite number of solutions.")
if (a == 0 and b != 0):
    print("No solutions.")
if (a != 0):
    print("X = {0}.".format(b/a))
2