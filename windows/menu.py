# Menu de opcoes para um arquivo

import os
import tkinter as tk

# Importa as funções necessárias
from functions.abrir_arquivo import abrir_arquivo
from functions.copiar_arquivo import copiar_arquivo
from functions.mover_arquivo import mover_arquivo
from functions.excluir_arquivo import excluir_arquivo
from functions.renomear_arquivo import renomear_arquivo

# Configuração de cores
COR_FUNDO = "#000000"  # Preto
COR_BOTAO = "#0000FF"  # Azul
COR_TEXTO = "#FFFFFF"  # Branco
COR_LISTA = "#333333"  # Cinza escuro

def menu_arquivo(caminho_arquivo):
    from windows.janela_principal import janela
    
    janela_menu = tk.Toplevel(janela)
    janela_menu.title("Menu do Arquivo")
    janela_menu.geometry("300x280")
    janela_menu.configure(bg=COR_FUNDO)
  
    # Label com o nome do arquivo
    tk.Label(janela_menu, 
             text=f"Arquivo: {os.path.basename(caminho_arquivo)}",
             bg=COR_FUNDO,
             fg=COR_TEXTO).pack(pady=10)
    
    # Botões do menu
    tk.Button(janela_menu, 
              text="Abrir", 
              command=lambda: [abrir_arquivo(caminho_arquivo), janela_menu.destroy()],
              bg=COR_BOTAO,
              fg=COR_TEXTO,
              activebackground=COR_BOTAO,
              activeforeground=COR_TEXTO).pack(fill=tk.X, padx=10, pady=5)
              
    tk.Button(janela_menu, 
              text="Copiar", 
              command=lambda: [copiar_arquivo(caminho_arquivo), janela_menu.destroy()],
              bg=COR_BOTAO,
              fg=COR_TEXTO,
              activebackground=COR_BOTAO,
              activeforeground=COR_TEXTO).pack(fill=tk.X, padx=10, pady=5)
              
    tk.Button(janela_menu, 
              text="Mover", 
              command=lambda: [mover_arquivo(caminho_arquivo), janela_menu.destroy()],
              bg=COR_BOTAO,
              fg=COR_TEXTO,
              activebackground=COR_BOTAO,
              activeforeground=COR_TEXTO).pack(fill=tk.X, padx=10, pady=5)
              
    tk.Button(janela_menu, 
              text="Renomear", 
              command=lambda: [renomear_arquivo(caminho_arquivo), janela_menu.destroy()],
              bg=COR_BOTAO,
              fg=COR_TEXTO,
              activebackground=COR_BOTAO,
              activeforeground=COR_TEXTO).pack(fill=tk.X, padx=10, pady=5)
              
    tk.Button(janela_menu, 
              text="Excluir", 
              command=lambda: [excluir_arquivo(caminho_arquivo), janela_menu.destroy()],
              bg=COR_BOTAO,
              fg=COR_TEXTO,
              activebackground=COR_BOTAO,
              activeforeground=COR_TEXTO).pack(fill=tk.X, padx=10, pady=5)
              
    tk.Button(janela_menu, 
              text="Cancelar",
              command=janela_menu.destroy,
              bg="#FF5252",
              fg=COR_TEXTO,
              activebackground="#FF5252",
              activeforeground=COR_TEXTO).pack(fill=tk.X, padx=10, pady=5) 