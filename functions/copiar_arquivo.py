# Copiar um arquivo

import os
import shutil
from tkinter import messagebox
import tkinter as tk
from database.banco import registrar_operacao

# Configuração de cores
COR_FUNDO = "#000000"  # Preto
COR_BOTAO = "#0000FF"  # Azul
COR_TEXTO = "#FFFFFF"  # Branco
COR_LISTA = "#333333"  # Cinza escuro

def copiar_arquivo(caminho_arquivo):
    from windows.janela_principal import janela, atualizar_lista, caminho_atual
    
    def confirmar_copiar():
        destino = entrada_destino.get()
        if destino and os.path.isdir(destino):
            try:
                nome_arquivo = os.path.basename(caminho_arquivo)
                novo_caminho = os.path.join(destino, nome_arquivo)
                
                # Verifica se o arquivo já existe no destino
                if os.path.exists(novo_caminho):
                    # Cria uma nova janela para perguntar ao usuário
                    janela_opcoes = tk.Toplevel(janela_copiar)
                    janela_opcoes.title("Arquivo já existe")
                    janela_opcoes.geometry("300x150")
                    janela_opcoes.configure(bg=COR_FUNDO)
                    
                    tk.Label(janela_opcoes,
                            text="O arquivo já existe no destino.\nO que deseja fazer?",
                            bg=COR_FUNDO,
                            fg=COR_TEXTO).pack(pady=10)
                    
                    def substituir():
                        shutil.copy2(caminho_arquivo, novo_caminho)
                        registrar_operacao(caminho_arquivo, "Copiar (Substituir)")
                        messagebox.showinfo("Sucesso", "Arquivo substituído com sucesso.")
                        janela_opcoes.destroy()
                        janela_copiar.destroy()
                        atualizar_lista(caminho_atual.get())
                    
                    def criar_copia():
                        # Encontra o próximo número disponível para a cópia
                        base, ext = os.path.splitext(nome_arquivo)
                        contador = 1
                        while True:
                            novo_nome = f"{base} ({contador}){ext}"
                            novo_caminho = os.path.join(destino, novo_nome)
                            if not os.path.exists(novo_caminho):
                                break
                            contador += 1
                        
                        shutil.copy2(caminho_arquivo, novo_caminho)
                        registrar_operacao(caminho_arquivo, f"Copiar (Cópia {contador})")
                        messagebox.showinfo("Sucesso", f"Arquivo copiado como '{novo_nome}' com sucesso.")
                        janela_opcoes.destroy()
                        janela_copiar.destroy()
                        atualizar_lista(caminho_atual.get())
                    
                    tk.Button(janela_opcoes,
                             text="Substituir",
                             command=substituir,
                             bg=COR_BOTAO,
                             fg=COR_TEXTO,
                             activebackground=COR_BOTAO,
                             activeforeground=COR_TEXTO).pack(pady=5)
                    
                    tk.Button(janela_opcoes,
                             text="Criar nova cópia",
                             command=criar_copia,
                             bg=COR_BOTAO,
                             fg=COR_TEXTO,
                             activebackground=COR_BOTAO,
                             activeforeground=COR_TEXTO).pack(pady=5)
                    
                    tk.Button(janela_opcoes,
                             text="Cancelar",
                             command=janela_opcoes.destroy,
                             bg="#FF5252",
                             fg=COR_TEXTO,
                             activebackground="#FF5252",
                             activeforeground=COR_TEXTO).pack(pady=5)
                else:
                    # Se o arquivo não existe, copia normalmente
                    shutil.copy2(caminho_arquivo, novo_caminho)
                    registrar_operacao(caminho_arquivo, "Copiar")
                    messagebox.showinfo("Sucesso", "Arquivo copiado com sucesso.")
                    janela_copiar.destroy()
                    atualizar_lista(caminho_atual.get())
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao copiar o arquivo: {e}")
        else:
            messagebox.showerror("Erro", "Caminho de destino inválido.")
                
    janela_copiar = tk.Toplevel(janela)
    janela_copiar.title("Copiar Arquivo")
    janela_copiar.geometry("400x200")
    janela_copiar.configure(bg=COR_FUNDO)

    tk.Label(janela_copiar, 
             text=f"Arquivo: {os.path.basename(caminho_arquivo)}",
             bg=COR_FUNDO,
             fg=COR_TEXTO).pack(pady=10)
             
    tk.Label(janela_copiar,
             text="Digite o caminho de destino:",
             bg=COR_FUNDO,
             fg=COR_TEXTO).pack(pady=5)
             
    entrada_destino = tk.Entry(janela_copiar, width=50, bg=COR_LISTA, fg=COR_TEXTO, insertbackground=COR_TEXTO)
    entrada_destino.pack(pady=5)

    tk.Button(janela_copiar,
              text="Copiar",
              command=confirmar_copiar,
              bg=COR_BOTAO,
              fg=COR_TEXTO,
              activebackground=COR_BOTAO,
              activeforeground=COR_TEXTO).pack(pady=10)

    tk.Button(janela_copiar,
              text="Cancelar",
              command=janela_copiar.destroy,
              bg="#FF5252",
              fg=COR_TEXTO,
              activebackground="#FF5252",
              activeforeground=COR_TEXTO).pack(pady=5) 