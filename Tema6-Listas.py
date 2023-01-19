lista=["Eric", 1, 2, True]

print(lista)


print(lista[:])
print(lista[2:3])
print(lista[3:])
lista.append("Fernando")

print(lista)

lista.extend([9, 10, 11])

print(lista)
print(lista.index("Eric"))
lista.remove("Fernando")

print(lista)

lista.pop()

print(lista)
