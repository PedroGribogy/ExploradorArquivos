# Mover um arquivo

import shutil # Permite fazer alteracoes no diretorio
from tkinter import messagebox # Importa a caixa de mensagem
import tkinter as tk # Permite criarmos uma interface grafica
from banco import registrar_operacao # Importa a funcao registrar_operacao
import os # Permite acesso ao sistema operacional

# mover_arquivo

def mover_arquivo(caminho_arquivo): # Cria uma funcao chamada mover_arquivo
    from janela_principal import janela # Importa a janela principal
    
    def confirmar_movimento():# Cria um subfuncao chamada confirmar_movimento
        destino = entrada_destino.get()  # Grava o local escolhido pelo usuario
        if destino: # Verifica se o usuario escolheu um caminho valido
            try: # Executa a tentiva de mover o arquivo
                # Verifica se o diretório de destino existe
                diretorio_destino = os.path.dirname(destino)
                if not os.path.exists(diretorio_destino):
                    os.makedirs(diretorio_destino)
                    
                shutil.move(caminho_arquivo, destino) # Move o arquivo
                registrar_operacao(caminho_arquivo, "Mover") # Registra o processo no banco
                messagebox.showinfo("Sucesso", "Arquivo movido com sucesso.") # Exibe a mensagem de sucesso ao usuario
                janela_destino.destroy() # Finaliza a caixa de mensagem
            except Exception as e: # Abre uma excecao em caso de erro
                messagebox.showerror("Erro", f"Erro ao mover o arquivo: {e}") # Exibe a mensagem de erro
                
    janela_destino = tk.Toplevel(janela) # Cria uma nova janela dentro da interface
    janela_destino.title("Selecionar Destino") # Titula a janela
    janela_destino.geometry("400x150") # Cria o tamanho da janela
    
    tk.Label(janela_destino, text="Digite o caminho do destino:").pack(pady=10) # Cria um texto na janela com instrucoes ao usuario
    entrada_destino = tk.Entry(janela_destino, width=50) # Cria um campo de entrada para o usuario digitar algo
    entrada_destino.pack(pady=5) # Ajusta posicao do widget na tela
    tk.Button(janela_destino, text="Confirmar", command=confirmar_movimento).pack(pady=10) # Cria uma botao confirmar

# Fim mover_arquivo
