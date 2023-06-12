cartas = ('Q', 'A')

orden = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1}
ordenadas = sorted(cartas, key=lambda carta: orden[carta], reverse=True)

print(ordenadas)

clavre = 