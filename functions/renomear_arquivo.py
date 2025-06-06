# Renomear um arquivo

import os
import tkinter as tk
from tkinter import messagebox
from database.banco import registrar_operacao

#Configuração de cores
COR_FUNDO = "#000000"  # Preto
COR_BOTAO = "#0000FF"  # Azul
COR_TEXTO = "#FFFFFF"  # Branco
COR_LISTA = "#333333"  # Cinza escuro

def renomear_arquivo(caminho_arquivo):
    from windows.janela_principal import janela, atualizar_lista, caminho_atual
    
    def confirmar_renomeacao():
        novo_nome = entrada_nome.get()
        if novo_nome:
            try:
                diretorio = os.path.dirname(caminho_arquivo)
                # Obtém a extensão do arquivo original
                _, extensao = os.path.splitext(caminho_arquivo)
                # Adiciona a extensão ao novo nome se não estiver presente
                if not novo_nome.endswith(extensao):
                    novo_nome = novo_nome + extensao
                novo_caminho = os.path.join(diretorio, novo_nome)
                os.rename(caminho_arquivo, novo_caminho)
                registrar_operacao(caminho_arquivo, "Renomear")
                messagebox.showinfo("Sucesso", "Arquivo renomeado com sucesso.")
                janela_renomear.destroy()
                # Atualiza a interface após renomear o arquivo
                atualizar_lista(caminho_atual.get())
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao renomear o arquivo: {e}")
                
    janela_renomear = tk.Toplevel(janela)
    janela_renomear.title("Renomear Arquivo")
    janela_renomear.geometry("400x150")
    janela_renomear.configure(bg=COR_FUNDO)

    # Obtém o nome base do arquivo (sem a extensão)
    nome_base = os.path.splitext(os.path.basename(caminho_arquivo))[0]
    extensao = os.path.splitext(caminho_arquivo)[1]

    tk.Label(janela_renomear, 
             text=f"Nome atual: {nome_base}{extensao}",
             bg=COR_FUNDO,
             fg=COR_TEXTO).pack(pady=10)
    tk.Label(janela_renomear, 
             text="Digite o novo nome (sem extensão):",
             bg=COR_FUNDO,
             fg=COR_TEXTO).pack(pady=5)
    entrada_nome = tk.Entry(janela_renomear, width=50, bg=COR_LISTA, fg=COR_TEXTO, insertbackground=COR_TEXTO)
    entrada_nome.insert(0, nome_base)
    entrada_nome.pack(pady=5)

    tk.Button(janela_renomear, 
              text="Confirmar",
              command=confirmar_renomeacao,
              bg=COR_BOTAO,
              fg=COR_TEXTO,
              activebackground=COR_BOTAO,
              activeforeground=COR_TEXTO).pack(pady=10)
    tk.Button(janela_renomear, 
              text="Cancelar",
              command=janela_renomear.destroy,
              bg="#FF5252",
              fg=COR_TEXTO,
              activebackground="#FF5252",
              activeforeground=COR_TEXTO).pack(pady=5) 