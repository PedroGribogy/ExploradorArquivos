# Abrir um arquivo

import os # Permite acesso ao sistema operaciona
from tkinter import messagebox # Importa a caixa de mensagens
from banco import registrar_operacao # Importa a funcao registrar_operacao

# abrir_arquivo

def abrir_arquivo(caminho_arquivo): # Abre uma funcao
    try:
        os.startfile(caminho_arquivo) # Pede ao sistema operacional para abrir o arquivo
        registrar_operacao(caminho_arquivo, "Abrir") # Registra a acao no bnco de dados
    except Exception as e: # Abre uma mensagem caso de errado
        messagebox.showerror("Erro", f"Erro ao abrir o arquivo: {e}") # Exibe a  mensagem de erro
        
# Fim abrir_arquivo