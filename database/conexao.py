import sqlite3
import csv

#conecta ao banco de dados
def conectar():
    return sqlite3.connect("banco.db")

#cria a tabela se não exixtir
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS transacoes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   descricao TEXT,
                   valor REAL,
                   categoria TEXT,
                   data TEXT
                   )
                   """)
    conn.commit()
    conn.close()

#Insere uma nova transação
def inserir_transacao(descricao, valor, categoria, data):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO transacoes (descricao, valor, categoria, data)
                   VALUES (?, ?, ?, ?)
                   """, (descricao, valor, categoria, data))
    conn.commit()
    conn.close()

# Busca todas as transações
def buscar_transacoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transacoes")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

# Remove uma transação pelo ID
def remover_transacao(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transacoes WHERE id = ?", (id,))
    conn.commit()
    conn.close()

# Calcula o resumo financeiro (total receitas, despesas e saldo)
def calcular_resumo():
    conn = conectar()
    cursor = conn.cursor()

    # receitas = valores positivos
    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE valor > 0")
    total_receitas = cursor.fetchone()[0] or 0

    # despesas = valores negativos
    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE valor < 0")
    total_despesas = cursor.fetchone()[0] or 0

    # saldo = receitas + despesas (despesas são negativas)
    saldo = total_receitas + total_despesas

    conn.close()
    return total_receitas, total_despesas, saldo

# Exporta as transações para um arquivo CSV
def exportar_transacoes_csv(nome_arquivo="transacoes_exportadas.csv"):
    transacoes = buscar_transacoes()
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Descricao", "Valor", "Categoria", "Data"])
        for t in transacoes:
            writer.writerow(t)

# Busca transações por categoria
def buscar_transacoes_por_categoria(categoria):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transacoes WHERE categoria = ?", (categoria,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado