# Exibir histórico de operações

import tkinter as tk
from tkinter import ttk
from database.banco import conectar_banco

# Configuração de cores
COR_FUNDO = "#000000"  # Preto
COR_BOTAO = "#0000FF"  # Azul
COR_TEXTO = "#F1F1F1"  # Branco
COR_LISTA = "#333333"  # Cinza escuro

def exibir_historico():
    from windows.janela_principal import janela
    
    janela_historico = tk.Toplevel(janela)
    janela_historico.title("Histórico de Operações")
    janela_historico.geometry("800x400")
    janela_historico.configure(bg=COR_FUNDO)
    
    # Cria a tabela
    style = ttk.Style()
    style.configure("Treeview", 
                   background=COR_LISTA,
                   foreground=COR_TEXTO,
                   fieldbackground=COR_LISTA)
    style.configure("Treeview.Heading",
                   background='black',
                   foreground='black')
                
    
    tabela = ttk.Treeview(janela_historico, columns=("Data/Hora", "Operação", "Caminho"), show="headings")
    tabela.heading("Data/Hora", text="Data/Hora")
    tabela.heading("Operação", text="Operação")
    tabela.heading("Caminho", text="Caminho")
    tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    try:
        # Buscar dados do banco
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT data_hora, operacao, caminho 
            FROM historico 
            ORDER BY data_hora DESC
        """)
        registros = cursor.fetchall()
        conn.close()
        
        # Inserir dados na tabela
        for registro in registros:
            tabela.insert("", "end", values=registro)
            
        if not registros:
            tk.Label(janela_historico, 
                    text="Nenhum registro encontrado no histórico.",
                    bg=COR_FUNDO,
                    fg=COR_TEXTO).pack(pady=10)
    except Exception as e:
        tk.Label(janela_historico, 
                text=f"Erro ao buscar histórico: {e}",
                bg=COR_FUNDO,
                fg=COR_TEXTO).pack(pady=10)
    
    # Botão para fechar
    tk.Button(janela_historico, 
              text="Fechar", 
              command=janela_historico.destroy,
              bg="#FF5252",  # Vermelho para o botão de fechar
              fg=COR_TEXTO,
              activebackground="#FF5252",
              activeforeground=COR_TEXTO).pack(pady=10) 