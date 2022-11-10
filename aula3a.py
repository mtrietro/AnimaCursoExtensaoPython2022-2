# loop
contador = 1
while (contador < 10):
  print(contador)
  contador += 1

# cria array & mostra todo o array, com aspas e []
cores = ["branco", "amarelo", "vermelho"]
print(cores) 

 # mostra apenas o elemento da posição
print(cores[1])

# mostra tamanho do array
print(len(cores)) 

# adiciona elemento no array
cores.append("preto") 
print(cores)

# mostra elementos do array em sequência
i = 0
while(i < len(cores)):
  print(cores[i])
  i += 1

for cor in cores:
  print(cor)