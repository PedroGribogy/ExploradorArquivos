# Selecionar um item na lista

import os
import tkinter as tk
from database.banco import registrar_operacao

def selecionar_item(event):
    try:
        from windows.janela_principal import lista_conteudo, caminho_atual, atualizar_lista
        from navigation.navegar_diretorios import caminhos_visitados
        
        selecionado = lista_conteudo.get(lista_conteudo.curselection())
        caminho_completo = os.path.join(caminho_atual.get(), selecionado)
        
        if os.path.isdir(caminho_completo):
            # Adiciona o caminho atual à pilha antes de mudar
            caminhos_visitados.append(caminho_atual.get())
            
            # Atualiza o caminho atual
            caminho_atual.set(caminho_completo)
            
            # Atualiza a lista com o novo conteúdo
            atualizar_lista(caminho_completo)
            
            # Registra a navegação
            registrar_operacao(caminho_completo, "Navegar")
        elif os.path.isfile(caminho_completo):
            from windows.menu import menu_arquivo
            menu_arquivo(caminho_completo)
    except tk.TclError:
        pass 