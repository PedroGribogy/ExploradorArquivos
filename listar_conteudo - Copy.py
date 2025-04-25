# Lista o conteudo que ha dentro de um diretorio

import os # Permite o acesso ao sistema operacional
from tkinter import messagebox # Importa a caixa de mensagem

# listar_conteudo

def listar_conteudo(caminho):
    try:
        if not os.path.isdir(caminho):
            messagebox.showerror("Erro", "O caminho especificado não é um diretório.")
            return []
        
        conteudo = os.listdir(caminho)
        if not conteudo:
            messagebox.showinfo("Aviso", "O diretório está vazio.")
        return conteudo
    except PermissionError:
        messagebox.showerror("Erro", "Permissao negada para acessar este diretorio")
        return []
    
# Fim listar_conteudo