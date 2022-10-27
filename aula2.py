# comando input
nome = input("Digite seu nome: ")
idade = int(input("E sua idade: "))
genero = input("Informe seu gênero (F, M ou O): ")
dobro = (idade * 2)

# exibir variáveis
print(f"Seu nome é {nome} e tens {idade} anos.")
print(f"O dobro da sua idade é {dobro}.")

if(idade >= 18):
  print("Você é maior de idade. Já pode dirigir ou beber.")
  if(genero == "M"):
    # ou if(idade >= 18 and genero == "M"):
    print("Também deves prestar serviço militar obrigatório.")
else:
  print("Você é menor de idade.")


