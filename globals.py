# Variáveis globais que serão inicializadas em janela_principal.py
filtro_atual = None
caminhos_visitados = []  # Armazena os caminhos visitados

def inicializar_variaveis(janela_tk):
    """Inicializa as variáveis globais que precisam da janela Tkinter"""
    global filtro_atual
    import tkinter as tk
    filtro_atual = tk.StringVar(janela_tk)
    filtro_atual.set("Todos")

