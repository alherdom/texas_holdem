def ordenar_por_frecuencia(values):
    return sorted(values, key=lambda v: values.count(v), reverse=True)

values = [5, 4, 3, 2, 1]
order_values = ordenar_por_frecuencia(values)
print(order_values)

pritn(sorted)

escalera = [2,3,4,5,14]