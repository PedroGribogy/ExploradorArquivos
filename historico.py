# Exibir histórico de ações

import tkinter as tk
from tkinter import ttk
from banco import conectar_banco
import os

def exibir_historico():
    from janela_principal import janela
    
    # Criar a janela do histórico
    janela_historico = tk.Toplevel(janela)
    janela_historico.title("Histórico de Ações")
    janela_historico.geometry("900x400")
    
    # Criar a tabela com a ordem correta das colunas
    tabela = ttk.Treeview(janela_historico, columns=("Data/Hora", "Operação", "Caminho"), show="headings")
    tabela.heading("Data/Hora", text="Data/Hora")
    tabela.heading("Operação", text="Operação")
    tabela.heading("Caminho", text="Caminho")
    
    # Configurar as colunas
    tabela.column("Data/Hora", width=150)
    tabela.column("Operação", width=100)
    tabela.column("Caminho", width=500)
    
    # Adicionar scrollbar
    scrollbar = ttk.Scrollbar(janela_historico, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=scrollbar.set)
    
    # Posicionar os widgets
    tabela.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    try:
        # Buscar dados do banco na ordem correta
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT data_hora, operacao, caminho 
            FROM historico 
            ORDER BY data_hora DESC
        """)
        registros = cursor.fetchall()
        conn.close()
        
        print(f"Total de registros encontrados: {len(registros)}")
        
        # Inserir dados na tabela
        for registro in registros:
            tabela.insert("", "end", values=registro)
            
        if not registros:
            tk.Label(janela_historico, text="Nenhum registro encontrado no histórico.").pack(pady=10)
    except Exception as e:
        print(f"Erro ao buscar histórico: {e}")
        tk.Label(janela_historico, text=f"Erro ao buscar histórico: {e}").pack(pady=10)
    
    # Botão para fechar
    tk.Button(janela_historico, text="Fechar", command=janela_historico.destroy).pack(pady=10) 