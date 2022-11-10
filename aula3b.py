# cria uma função --> calcula imposto de 5%

def calcularImposto(valor):
  imposto = valor * 0.05
  return print(f"O imposto de R${valor} é R${imposto}.")

calcularImposto(100)

# precos = [100, 1.99, 19.80]
# for preco in precos:
#  print(calcularImposto(preco))

def calcularImpostoAliquota(valor, aliquota):
  imposto = valor * (aliquota / 100)
  return print(f"O imposto de R${valor} é R${imposto}.")

calcularImpostoAliquota(100, 5)