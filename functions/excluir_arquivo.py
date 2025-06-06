# Excluir um arquivo

import os
from tkinter import messagebox
import tkinter as tk
from database.banco import registrar_operacao

#Configuração de cores
COR_FUNDO = "#000000"  # Preto
COR_BOTAO = "#0000FF"  # Azul
COR_TEXTO = "#FFFFFF"  # Branco
COR_LISTA = "#333333"  # Cinza escuro

def excluir_arquivo(caminho_arquivo):
    from windows.janela_principal import janela, atualizar_lista, caminho_atual
    
    def confirmar_exclusao():
        try:
            os.remove(caminho_arquivo)
            registrar_operacao(caminho_arquivo, "Excluir")
            messagebox.showinfo("Sucesso", "Arquivo excluído com sucesso.")
            janela_exclusao.destroy()
            # Atualiza a interface após excluir o arquivo
            atualizar_lista(caminho_atual.get())
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir o arquivo: {e}")
            
    janela_exclusao = tk.Toplevel(janela)
    janela_exclusao.title("Confirmar Exclusão")
    janela_exclusao.geometry("400x150")
    janela_exclusao.configure(bg=COR_FUNDO)

    tk.Label(janela_exclusao, 
             text=f"Tem certeza que deseja excluir o arquivo:\n{caminho_arquivo}?",
             bg=COR_FUNDO,
             fg=COR_TEXTO).pack(pady=10)
             
    tk.Button(janela_exclusao, 
              text="Confirmar Exclusão", 
              command=confirmar_exclusao,
              bg=COR_BOTAO,
              fg=COR_TEXTO,
              activebackground=COR_BOTAO,
              activeforeground=COR_TEXTO).pack(pady=10)
    tk.Button(janela_exclusao, 
              text="Cancelar",
              command=janela_exclusao.destroy,
              bg="#FF5252",
              fg=COR_TEXTO,
              activebackground="#FF5252",
              activeforeground=COR_TEXTO).pack(pady=5) 