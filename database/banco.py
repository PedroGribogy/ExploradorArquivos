# Arquivo para operações com o banco de dados

import sqlite3
import os
from datetime import datetime

# Caminho absoluto para o banco de dados na pasta database
BANCO_DADOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'historico.db')

def conectar_banco():
    """Conecta ao banco de dados SQLite e cria a tabela se não existir"""
    try:
        print(f"Conectando ao banco de dados em: {BANCO_DADOS}")
        
        # Conecta ao banco de dados
        conn = sqlite3.connect(BANCO_DADOS)
        
        # Cria a tabela se não existir
        cursor = conn.cursor()
        print("Criando tabela historico...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS historico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_hora DATETIME,
                operacao TEXT,
                caminho TEXT
            )
        """)
        conn.commit()
        
        # Verifica se a tabela foi criada
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='historico'")
        if cursor.fetchone():
            print("Tabela historico criada com sucesso!")
        else:
            print("ERRO: Tabela historico não foi criada!")
        
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def registrar_operacao(caminho, operacao):
    """Registra uma operação no banco de dados"""
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        print(f"Registrando operação: {operacao} em {caminho}")
        cursor.execute("""
            INSERT INTO historico (data_hora, operacao, caminho)
            VALUES (?, ?, ?)
        """, (datetime.now()strftime('%Y-%m-%d %H:%M:%S'), operacao, caminho))
        conn.commit()
        conn.close()
        print("Operação registrada com sucesso!")
    except Exception as e:
        print(f"Erro ao registrar operação: {e}")
        if 'conn' in locals():
            conn.close()
        raise 
