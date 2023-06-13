lista = [2, 3, 2, 3, 5]
resultado = sorted(lista, key=lambda x: (-lista.count(x), x))
print(resultado)

if [2, 3, 2, 3, 5] == [2, 3, 2, 3, 4]:
    print(True)
else:
    print(False)