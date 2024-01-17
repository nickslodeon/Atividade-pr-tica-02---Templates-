import sqlite3

db_file = 'clientes.db'  # Adição da extensão .db ao nome do arquivo
conn = sqlite3.connect(db_file)

cursor = conn.cursor()

# Alteração na estrutura da tabela para incluir um ID único para cada registro
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY,
        candidatos TEXT,
        users TEXT
    )
''')

# Inserção de dados com identificador único
cursor.execute('INSERT INTO clientes(candidatos, users) VALUES (?,?)', ('joão', 'jooaaooo'))
cursor.execute('INSERT INTO clientes(candidatos, users) VALUES (?,?)', ('fabio', 'fabs'))

conn.commit()

# Seleção e impressão dos dados
cursor.execute('SELECT * FROM clientes')
for row in cursor.fetchall():
    print(row)

conn.close()
