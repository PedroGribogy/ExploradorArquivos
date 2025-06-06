# Selecionar um disco

import os
import tkinter as tk
from database.banco import registrar_operacao

# Configuração de cores
COR_FUNDO = "#000000"  # Preto
COR_BOTAO = "#0000FF"  # Azul
COR_TEXTO = "#FFFFFF"  # Branco
COR_LISTA = "#333333"  # Cinza escuro

def selecionar_disco():
    from windows.janela_principal import discos_var, caminho_atual, atualizar_lista, janela
    
    disco = discos_var.get()
    if disco:
        # Cria uma janela para selecionar a pasta
        janela_pastas = tk.Toplevel(janela)
        janela_pastas.title("Selecionar Pasta")
        janela_pastas.geometry("300x400")
        janela_pastas.configure(bg=COR_FUNDO)
        
        # Obtém o caminho do usuário
        usuario = os.getenv("USERNAME")
        caminho_usuario = os.path.join(disco, "Users", usuario)
        
        # Lista de pastas comuns do Windows
        pastas_comuns = [
            ("Documentos", os.path.join(caminho_usuario, "Documents")),
            ("Imagens", os.path.join(caminho_usuario, "Pictures")),
            ("Downloads", os.path.join(caminho_usuario, "Downloads")),
            ("Músicas", os.path.join(caminho_usuario, "Music")),
            ("Vídeos", os.path.join(caminho_usuario, "Videos")),
            ("Área de Trabalho", os.path.join(caminho_usuario, "Desktop")),
            ("Ver Todo o Disco", disco)
        ]
        
        # Label com instruções
        tk.Label(janela_pastas,
                text="Selecione uma pasta:",
                bg=COR_FUNDO,
                fg=COR_TEXTO,
                font=("Arial", 12, "bold")).pack(pady=10)
        
        # Cria botões para cada pasta
        for nome_pasta, caminho_pasta in pastas_comuns:
            if os.path.exists(caminho_pasta) or nome_pasta == "Ver Todo o Disco":
                tk.Button(janela_pastas,
                         text=nome_pasta,
                         command=lambda c=caminho_pasta: [caminho_atual.set(c), 
                                                        atualizar_lista(c),
                                                        janela_pastas.destroy(),
                                                        registrar_operacao(c, "Abrir Pasta")],
                         bg=COR_BOTAO,
                         fg=COR_TEXTO,
                         activebackground=COR_BOTAO,
                         activeforeground=COR_TEXTO,
                         width=25).pack(pady=5)
        
        # Botão para cancelar
        tk.Button(janela_pastas,
                 text="Cancelar",
                 command=janela_pastas.destroy,
                 bg="#FF5252",
                 fg=COR_TEXTO,
                 activebackground="#FF5252",
                 activeforeground=COR_TEXTO,
                 width=25).pack(pady=10) 