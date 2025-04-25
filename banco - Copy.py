import sqlite3 # Faz a conexao com o banco
from datetime import datetime # Importa data e hora
import os # Permite acesso ao sistema operacional
from tkinter import messagebox # Importa a caixa de mensagem


# Conectar ao banco de dados e criar a tabela se não existir
# conectar_banco

def conectar_banco():
    try:
        # Criar o diretório se não existir
        diretorio = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Execucoes")
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f"Diretório criado: {diretorio}")
        
        # Caminho do banco de dados
        caminho_banco = os.path.join(diretorio, "execucoes.db")
        print(f"Tentando conectar ao banco de dados: {caminho_banco}")
        
        # Conectar ao banco
        conn = sqlite3.connect(caminho_banco)
        cursor = conn.cursor()
        
        # Criar tabela se não existir com a ordem correta das colunas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS historico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_hora TEXT NOT NULL,
                operacao TEXT NOT NULL,
                caminho TEXT NOT NULL
            )
        """)
        conn.commit()
        print("Conexão com o banco de dados estabelecida com sucesso")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None

# Fim "conectar_banco"


# Registrar operação no banco de dados
# registrar_operacao

def registrar_operacao(caminho, operacao):
    try:
        conn = conectar_banco()
        if conn is None:
            return
            
        cursor = conn.cursor()
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"Tentando registrar operação: {operacao} em {caminho}")
        
        # Inserir dados na ordem correta (data_hora, operacao, caminho)
        cursor.execute("""
            INSERT INTO historico (data_hora, operacao, caminho) 
            VALUES (?, ?, ?)
        """, (data_hora, operacao, caminho))
        conn.commit()
        conn.close()
        print(f"Operação registrada com sucesso: {operacao} em {caminho} às {data_hora}")
    except Exception as e:
        print(f"Erro ao registrar operação: {e}")
        messagebox.showerror("Erro", f"Erro ao registrar operação: {e}")
    
# Fim "registrar_operacao"
