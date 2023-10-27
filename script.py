import sqlite3
import os

def criar_tabela():
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def inserir_dados_arquivo():
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()
    
    with open('dados.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            nome = dados[0]
            idade = int(dados[1])
            cursor.execute("INSERT INTO dados (nome, idade) VALUES (?, ?)", (nome, idade))
    
    conn.commit()
    conn.close()

def ler_dados():
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados")
    dados = cursor.fetchall()
    conn.close()
    return dados

def atualizar_dados(id, novo_nome, nova_idade):
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE dados SET nome = ?, idade = ? WHERE id = ?", (novo_nome, nova_idade, id))
    conn.commit()
    conn.close()

def deletar_dados(id):
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dados WHERE id = ?", (id,))
    conn.commit()
    conn.close()

criar_tabela()
inserir_dados_arquivo()

inserir_dados = ("Ronaldo", 19)
conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO dados (nome, idade) VALUES (?, ?)", inserir_dados)
conn.commit()
conn.close()

dados = ler_dados()
print("Dados na tabela:")
for dado in dados:
    print(dado)

atualizar_dados(1, "Novo Nome", 25)
deletar_dados(2)
