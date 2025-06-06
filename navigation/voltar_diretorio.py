# Voltar para o diretorio anterior

from tkinter import messagebox
import os
from database.banco import registrar_operacao
from navigation.navegar_diretorios import caminhos_visitados

def voltar_diretorio():
    from windows.janela_principal import caminho_atual, atualizar_lista
    
    if caminhos_visitados:
        # Pega o caminho anterior
        caminho_anterior = caminhos_visitados.pop()
        
        # Atualiza o caminho atual
        caminho_atual.set(caminho_anterior)
        
        # Mantém o filtro atual e atualiza a lista
        atualizar_lista(caminho_anterior)
        
        # Registra a navegação
        registrar_operacao(caminho_anterior, "Voltar")
    else:
        messagebox.showinfo("Aviso", "Nao ha diretorios anteriores para voltar.") 