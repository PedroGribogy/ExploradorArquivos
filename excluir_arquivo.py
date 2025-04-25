# Excluir arquivo

import os # Permite acesso ao sistema operacional
from tkinter import messagebox # Importa a caixa de mensagem
from banco import registrar_operacao # Importa a funcao registrar_operacao

# Funcao excluir_arquivo

def excluir_arquivo (caminho_arquivo): # Funcao de excluir o arquivo
    confirmacao = messagebox.askyesno("Confirmacao", f"Tem certeza que deseja excluir o arquivo '{caminho_arquivo}'?") # Mensagem de confirmacao para excluir o arquivo
    if confirmacao: # Validacao da confirmacao
        try: # Tentativa de remover o arquivo
            os.remove(caminho_arquivo) # Remove o arquivo
            registrar_operacao(caminho_arquivo, "Excluir") # Registra a operacao no banco
            messagebox.showinfo("Operacao Concluida", "Arquivo excluido com sucesso") # Exibe a mensagem de sucesso ao excluir o arquivo
        except Exception as e: # Abre uma excecao caso exista erro na operacao
            messagebox.showerror("Erro", f"Erro ao excluir o arquivo: {e}") # Exibe mensagem de erro ao tentar excluir o arquivo
            
# Fim excluir_arquivo
            