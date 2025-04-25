# Copiar um arquivo

from tkinter import messagebox # Importa a caixa de mensagem
import shutil # Import que nos permite fazer alteracos no diretorio
import tkinter as tk # Nos permite criar interfaces graficas
from banco import registrar_operacao # Importa a funcao registrar_operacao

# copiar_arquivo

def copiar_arquivo(caminho_arquivo): # Cria uma funcao copiar_arquivo
    from janela_principal import janela # Importa a janela principal
    
    def confirmar_copia(): # Cria uma funcao para confirmar a copia
        destino = entrada_destino.get() # Armazena o caminho que o usuario digitar
        if destino: # Verifica se o destino foi preenchido
            try: 
                shutil.copy(caminho_arquivo, destino) # Tenta copiar o arquivo para o caminho do usuario
                registrar_operacao(caminho_arquivo, "Copiar") # Registar o processo no banco de dados
                messagebox.showinfo("Sucesso", "Arquivo copiado com sucesso.") # Exibi uma mensagem de sucesso caso o programa seja executado corretamente
                janela_destino.destroy() # Fecha a janela
            except Exception as e: # Exibi uma mensagem caso exista algum erro
                messagebox.showerror("Erro", f"Erro ao copiar o arquivo: {e}") # Mensagem de erro

    janela_destino = tk.Toplevel(janela) # Cria uma janela secundaria
    janela_destino.title("Selecionar Destino") # Define o titulo
    janela_destino.geometry("400x150") # Define o tamanho

    tk.Label(janela_destino, text="Digite o caminho do destino:").pack(pady=10) # Exebi uma mensagem requerindo o caminho
    entrada_destino = tk.Entry(janela_destino, width=50) # Campo onde o usuario digita o caminho
    entrada_destino.pack(pady=5) # Continuacao do campo de entrada
    tk.Button(janela_destino, text="Confirmar", command=confirmar_copia).pack(pady=10) # Botao de confirmar copia

# Fim copiar_arquivo