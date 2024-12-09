def contar(lista):
  pares = list(filter(lambda x: x % 2 == 0, lista))
  impares = list(filter(lambda x: x % 2 != 0, lista))
  return len(pares), len(impares)

lista = [2, 4, 6, 9, 10, 44, 34]
pares, impares = contar(lista)

print(pares)
print(impares)


