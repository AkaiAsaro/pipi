def letras(letras):
  return [ i for i in letras if len(i) > 4 ]

cores = ("azul", "vermelho", "verde","amarelo")

strings = letras(cores)
print(strings)