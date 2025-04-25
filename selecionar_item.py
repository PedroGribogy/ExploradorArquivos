# Selecionar um item na lista

import os # Permite acesso ao sistema operacional
import tkinter as tk # Permite criar uma interface grafica
from banco import registrar_operacao # Importa a função para registrar operações

# Funcao selecionar_item

def selecionar_item(event): # Cria a funcao selecionar_item
    try: # Tentativa de selecionar o item
        from janela_principal import lista_conteudo, caminho_atual, atualizar_lista # Importa as funcoes necessarias
        from voltar_diretorio import caminhos_visitados # Importa a pilha de caminhos visitados
        
        selecionado = lista_conteudo.get(lista_conteudo.curselection()) # Busca o item selecionado na lista
        caminho_completo = os.path.join(caminho_atual.get(), selecionado) # Constrói o caminho completo
        
        if os.path.isdir(caminho_completo): # Verifica se o item selecionado e um diretorio
            # Adiciona o caminho atual à pilha antes de mudar
            caminhos_visitados.append(caminho_atual.get())
            
            # Atualiza o caminho atual
            caminho_atual.set(caminho_completo)
            
            # Atualiza a lista com o novo conteúdo
            atualizar_lista(caminho_completo)
            
            # Registra a navegação
            registrar_operacao(caminho_completo, "Navegar")
        elif os.path.isfile(caminho_completo): # Verifica se o item selecionado e um arquivo
            from menu import menu_arquivo # Importa a funcao que abre o menu do arquivo
            menu_arquivo(caminho_completo) # Exibe o menu de opcoes
    except tk.TclError: # Excecao caso o usuario nao seleciona uma opcao
        pass # Ignora o erro
            
# Fim selecionar_item