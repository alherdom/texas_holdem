lista = [2, 3, 2, 3, 5]
resultado = sorted(lista, key=lambda x: (-lista.count(x), x))
print(resultado)

if [2, 3, 2, 3, 5] == [2, 3, 2, 3, 4]:
    print(True)
else:
    print(False)
    
values = [2, 3, 2, 3, 5]
values2 = [5, 3, 2, 3, 5]
print(sum(values))
print(sum(values2))
print(max(values, values2))
print(sorted(values,reverse=True))