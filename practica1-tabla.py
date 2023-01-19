
print(" ----- tabla de multiplicar ----")

print(" Introduce el número del cual quieras la tabla : ")

variable  = int(input("> "))

def printTable(number):
    for x in range(1, 11):
        print("{0} x {1} = {2}".format(number, x, number * x))

printTable(variable)
