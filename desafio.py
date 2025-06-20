import sqlite3

# Conectar ao banco
conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

#  Limpa as tabelas para evitar duplicações a cada execução
cursor.execute("DELETE FROM SELECAO_TESTE")
cursor.execute("DELETE FROM SELECAO_CANDIDATO")

# Criar a tabela SELECAO_CANDIDATO
cursor.execute('''
CREATE TABLE IF NOT EXISTS SELECAO_CANDIDATO (
    ID_CANDIDATO INTEGER PRIMARY KEY AUTOINCREMENT,
    NME_CANDIDATO TEXT NOT NULL,
    DAT_INSCRICAO TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Criar a tabela SELECAO_TESTE
cursor.execute('''
CREATE TABLE IF NOT EXISTS SELECAO_TESTE (
    ID_TESTE INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_CANDIDATO INTEGER,
    NUM_FIBONACCI INTEGER,
    NUM_PAR INTEGER CHECK (NUM_PAR IN (0, 1)),
    NUM_IMPAR INTEGER CHECK (NUM_IMPAR IN (0, 1)),
    FOREIGN KEY (ID_CANDIDATO) REFERENCES SELECAO_CANDIDATO(ID_CANDIDATO)
)
''')

# Inserir um candidato
cursor.execute("INSERT INTO SELECAO_CANDIDATO (NME_CANDIDATO) VALUES (?)", ("João da Silva",))
id_candidato = cursor.lastrowid

# Função Fibonacci
def fibonacci(n):
    numFib = [1, 1]
    while len(numFib) < n:
        numFib.append(numFib[-1] + numFib[-2])
    return numFib

# Gerar sequência
fib = fibonacci(30)

# Inserir Fibonacci no banco
for num in fib:
    par = 1 if num % 2 == 0 else 0
    impar = 1 if num % 2 != 0 else 0
    cursor.execute('''
        INSERT INTO SELECAO_TESTE (ID_CANDIDATO, NUM_FIBONACCI, NUM_PAR, NUM_IMPAR)
        VALUES (?, ?, ?, ?)
    ''', (id_candidato, num, par, impar))

conexao.commit()

# Consultas
print("\n--- Sistema de seleção de candidatos ---")
print("\n--- Sequência de Fibonacci completa ---")
print(", ".join(str(row[0]) for row in cursor.execute("SELECT NUM_FIBONACCI FROM SELECAO_TESTE ORDER BY ID_TESTE")))

print("\n5 maiores números da sequência:")
cursor.execute("SELECT NUM_FIBONACCI FROM SELECAO_TESTE ORDER BY NUM_FIBONACCI DESC LIMIT 5")
for row in cursor.fetchall():
    print(row[0])

# Contagem de pares e ímpares
print("\nContagem de pares e ímpares:")
cursor.execute("SELECT COUNT(*) FROM SELECAO_TESTE WHERE NUM_PAR = 1")
pares = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM SELECAO_TESTE WHERE NUM_IMPAR = 1")
impares = cursor.fetchone()[0]
print(f"Pares: {pares}, Ímpares: {impares}")

# Deletar números maiores que 5000
print("\n--- Deletando números maiores que 5000 ---")
cursor.execute("DELETE FROM SELECAO_TESTE WHERE NUM_FIBONACCI > 5000")
conexao.commit()

# Nova listagem
print("\nSequência Fibonacci atualizada:")
print(", ".join(str(row[0]) for row in cursor.execute("SELECT NUM_FIBONACCI FROM SELECAO_TESTE ORDER BY ID_TESTE")))

# Fechar conexão
conexao.close()
