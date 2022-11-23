# importa biblioteca
import sqlite3

# estabelece conexão
conexao = sqlite3.connect("dc_universe.db")

# cria objeto cursor
cursor = conexao.cursor()

# criar comando sql e executar
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"
cursor.execute(sql)

# exibir todos os nomes do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

# exibir nome fictício e civil
for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[2]})")

# exibir status
for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[2]})")