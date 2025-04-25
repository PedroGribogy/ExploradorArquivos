# Navegar por diretorios

import os # Permite acesso ao sistema operacional
import tkinter as tk # Permite criar uma interface grafica
from listar_conteudo import listar_conteudo # Importa a função para listar o conteúdo
from banco import registrar_operacao # Importa a funcao de registrar as operacoes

# Pilha para armazenar os caminho visitados
caminhos_visitados = [] # Armazena os camnhos visitados

# Fim pilha

# Funcao navegar_diretorios
def navegar_diretorios(caminho): # Funcao para navegar pelos diretorios
    from janela_principal import caminho_atual, lista_conteudo # Importa aas funcoes que mostra o caminho atual e que lista o conteudo
    
    if caminho_atual.get(): # Verifica se a um valor armazenado na variavel
        caminhos_visitados.append(caminho_atual.get()) # Adiciona o caminho atual
    
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
        
# Fim navegar_diretorios