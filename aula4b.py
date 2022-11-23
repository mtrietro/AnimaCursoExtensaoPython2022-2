# importa biblioteca
import sqlite3

# estabelece conexão
conexao = sqlite3.connect("dc_universe.db")

# cria objeto cursor
cursor = conexao.cursor()

# criar comando sql e executar
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'nome', 'nome civil', 'Herói(na)')"
cursor.execute(sql)
conexao.commit()
conexao.close()