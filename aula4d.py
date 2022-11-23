import aula4c as bd

con, cur = bd.conectar()

nome = input("Informe o nome fictício: ")
nome_civil = input("Informe o nome civil: ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o)")

# busca maior valor usado no banco
sql = "SELECT MAX(pessoa_id) FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)
con.commit()
con.close()