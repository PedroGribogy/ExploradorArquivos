# Voltar para o diretorio anterior

from tkinter import messagebox # Permite criar uma interface grafica
import os # Permite acesso ao sistema operacional
from banco import registrar_operacao # Importa a função para registrar operações
from globals import filtro_atual, caminhos_visitados # Importa as variáveis globais

# Funcao voltar_diretorio
def voltar_diretorio(): # Abre a funcao voltar_diretorio
    from janela_principal import caminho_atual, atualizar_lista # Importa as funcoes necessarias
    
    if caminhos_visitados: # Verifica se contem algum caminho para voltar
        # Pega o caminho anterior
        caminho_anterior = caminhos_visitados.pop()
        
        # Atualiza o caminho atual
        caminho_atual.set(caminho_anterior)
        
        # Mantém o filtro atual e atualiza a lista
        atualizar_lista(caminho_anterior)
        
        # Registra a navegação
        registrar_operacao(caminho_anterior, "Voltar")
    else: # Exibe uma mensagem caso nao haja diretórios anteriores
        messagebox.showinfo("Aviso", "Nao ha diretorios anteriores para voltar.")
        
# Fim voltar_diretorio
        