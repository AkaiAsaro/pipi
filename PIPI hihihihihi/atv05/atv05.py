def mais_vendas(vendas):

  mais_vendido = max(vendas.values())
  produtos_mais_vendidos = [produto for produto, qtd in vendas.items() if qtd == mais_vendido]

  return produtos_mais_vendidos

vendas = {
  "coca cola": 200,
  "fanta": 150,
  "pepsi": 200,
  "guaraná": 10
}
print(mais_vendas(vendas))