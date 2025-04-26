# Copiar um arquivo

import os
import shutil
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from database.banco import registrar_operacao

# Configuração de cores
COR_FUNDO = "#000000"  # Preto
COR_BOTAO = "#0000FF"  # Azul
COR_TEXTO = "#FFFFFF"  # Branco
COR_LISTA = "#333333"  # Cinza escuro

def copiar_arquivo(caminho_arquivo):
    from windows.janela_principal import janela
    
    def selecionar_destino():
        destino = filedialog.askdirectory()
        if destino:
            try:
                nome_arquivo = os.path.basename(caminho_arquivo)
                novo_caminho = os.path.join(destino, nome_arquivo)
                shutil.copy2(caminho_arquivo, novo_caminho)
                registrar_operacao(caminho_arquivo, "Copiar")
                messagebox.showinfo("Sucesso", "Arquivo copiado com sucesso.")
                janela_copiar.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao copiar o arquivo: {e}")
                
    janela_copiar = tk.Toplevel(janela)
    janela_copiar.title("Copiar Arquivo")
    janela_copiar.geometry("400x150")
    janela_copiar.configure(bg=COR_FUNDO)

    tk.Label(janela_copiar, 
             text=f"Arquivo: {os.path.basename(caminho_arquivo)}",
             bg=COR_FUNDO,
             fg=COR_TEXTO).pack(pady=10)
             
    tk.Button(janela_copiar,
              text="Escolher Destino",
              command=selecionar_destino,
              bg=COR_BOTAO,
              fg=COR_TEXTO,
              activebackground=COR_BOTAO,
              activeforeground=COR_TEXTO).pack(pady=10)

    tk.Button(janela_copiar,
              text="Cancelar",
              command=janela_copiar.destroy,
              bg="#FF5252",
              fg=COR_TEXTO,
              activebackground="#FF5252",
              activeforeground=COR_TEXTO).pack(pady=5) 