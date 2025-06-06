# Mover um arquivo

import os
import shutil
from tkinter import messagebox
import tkinter as tk
from database.banco import registrar_operacao

#Configuração de cores
COR_FUNDO = "#000000"  # Preto
COR_BOTAO = "#0000FF"  # Azul
COR_TEXTO = "#FFFFFF"  # Branco
COR_LISTA = "#333333"  # Cinza escuro

def mover_arquivo(caminho_arquivo):
    from windows.janela_principal import janela, atualizar_lista, caminho_atual
    
    def confirmar_mover():
        destino = entrada_destino.get()
        if destino and os.path.isdir(destino):
            try:
                nome_arquivo = os.path.basename(caminho_arquivo)
                novo_caminho = os.path.join(destino, nome_arquivo)
                shutil.move(caminho_arquivo, novo_caminho)
                registrar_operacao(caminho_arquivo, "Mover")
                messagebox.showinfo("Sucesso", "Arquivo movido com sucesso.")
                janela_mover.destroy()
                # Atualiza a interface após mover o arquivo
                atualizar_lista(caminho_atual.get())
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao mover o arquivo: {e}")
        else:
            messagebox.showerror("Erro", "Caminho de destino inválido.")
                
    janela_mover = tk.Toplevel(janela)
    janela_mover.title("Mover Arquivo")
    janela_mover.geometry("400x200")
    janela_mover.configure(bg=COR_FUNDO)

    tk.Label(janela_mover, 
             text=f"Arquivo: {os.path.basename(caminho_arquivo)}",
             bg=COR_FUNDO,
             fg=COR_TEXTO).pack(pady=10)
             
    tk.Label(janela_mover,
             text="Digite o caminho de destino:",
             bg=COR_FUNDO,
             fg=COR_TEXTO).pack(pady=5)
             
    entrada_destino = tk.Entry(janela_mover, width=50, bg=COR_LISTA, fg=COR_TEXTO, insertbackground=COR_TEXTO)
    entrada_destino.pack(pady=5)

    tk.Button(janela_mover,
              text="Mover",
              command=confirmar_mover,
              bg=COR_BOTAO,
              fg=COR_TEXTO,
              activebackground=COR_BOTAO,
              activeforeground=COR_TEXTO).pack(pady=10)

    tk.Button(janela_mover,
              text="Cancelar",
              command=janela_mover.destroy,
              bg="#FF5252",
              fg=COR_TEXTO,
              activebackground="#FF5252",
              activeforeground=COR_TEXTO).pack(pady=5) 