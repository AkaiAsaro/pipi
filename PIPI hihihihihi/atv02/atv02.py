produtos = []

def additens():
  produto = {}
  produto["produto"] = input("digite o nome do produto: ")
  produto["preço"] = float(input("digite o preço do produto: "))
  produto["quantidade"] = int(input("digite a quantidade do produto: "))
  produtos.append(produto)
  return produtos

additens()

print(produtos)