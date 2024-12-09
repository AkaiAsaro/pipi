def pares(pares):
  return [ i for i in pares if i % 2 == 0]

lista = [2, 5, 78, 99, 100, 1, 4, 7, 8, 10]
tudo = pares(lista)

print(tudo)



