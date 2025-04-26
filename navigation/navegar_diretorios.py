# Navegar por diretorios

import os
import tkinter as tk
from navigation.listar_conteudo import listar_conteudo
from database.banco import registrar_operacao

# Pilha para armazenar os caminho visitados
caminhos_visitados = []

def navegar_diretorios(caminho):
    from windows.janela_principal import caminho_atual, lista_conteudo
    
    if caminho_atual.get():
        caminhos_visitados.append(caminho_atual.get())
    
    # Atualiza o caminho atual
    caminho_atual.set(caminho)
    
    # Limpa a lista atual
    lista_conteudo.delete(0, tk.END)
    
    # Obtém o conteúdo do diretório
    conteudo = listar_conteudo(caminho)
    
    # Insere cada item na lista
    for item in conteudo:
        lista_conteudo.insert(tk.END, item)
    
    # Registra a operação no banco
    registrar_operacao(caminho, "Navegar") 