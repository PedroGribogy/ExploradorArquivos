# Abrir um arquivo

import os
from tkinter import messagebox
from database.banco import registrar_operacao

def abrir_arquivo(caminho_arquivo):
    try:
        os.startfile(caminho_arquivo)
        registrar_operacao(caminho_arquivo, "Abrir")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao abrir o arquivo: {e}") 