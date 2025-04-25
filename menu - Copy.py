# Menu de opcoes para um arquivo

import os # Permite acesso ao sistema operacional
import tkinter as tk # Permite criar uma interface grafica

# Importa as funções necessárias
from abrir_arquivo import abrir_arquivo
from copiar_arquivo import copiar_arquivo
from mover_arquivo import mover_arquivo
from excluir_arquivo import excluir_arquivo

# Funcao menu_arquivo

def menu_arquivo(caminho_arquivo): # Cria a funcao menu_arquivo
    from janela_principal import janela # Importa a janela principal
    
    janela_menu = tk.Toplevel(janela) # Cria uma janela de menu
    janela_menu.title("Menu do Arquivo") # Titula a janela
    janela_menu.geometry("300x200") # Ajusta o tamanho da janela
  
    tk.Label(janela_menu, text=f"Arquivo: {os.path.basename(caminho_arquivo)}").pack(pady=10) # Exibe uma mensagem mostrando qual e o arquivo
    
    tk.Button(janela_menu, text="Abrir", command=lambda: [abrir_arquivo(caminho_arquivo), janela_menu.destroy()]).pack(fill=tk.X, padx=10, pady=5) # Cria um botao de abrir arquivo
    
    tk.Button(janela_menu, text="Copiar", command=lambda: [copiar_arquivo(caminho_arquivo), janela_menu.destroy()]).pack(fill=tk.X, padx=10, pady=5) # Cria um botao de copiar o arquivo
    
    tk.Button(janela_menu, text="Mover", command=lambda: [mover_arquivo(caminho_arquivo), janela_menu.destroy()]).pack(fill=tk.X, padx=10, pady=5) # Cria um botao de mover o arquivo
    
    tk.Button(janela_menu, text="Excluir", command=lambda: [excluir_arquivo(caminho_arquivo), janela_menu.destroy()]).pack(fill=tk.X, padx=10, pady=5) # Cria um botao de excluir o arquivo
    
    tk.Button(janela_menu, text="Fechar", command=janela_menu.destroy).pack(fill=tk.X, padx=10, pady=5) # Cria um botao para fechar a janela

# Fim menu_arquivo