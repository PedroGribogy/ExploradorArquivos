# Configuaracao da janela principal

import tkinter as tk
import os
from navigation.listar_discos import listar_discos
from navigation.selecionar_disco import selecionar_disco
from navigation.voltar_diretorio import voltar_diretorio
from navigation.selecionar_item import selecionar_item
from navigation.listar_conteudo import listar_conteudo
from navigation.monitorar_diretorio import iniciar_monitoramento, parar_monitoramento
import globals
from windows.historico import exibir_historico
import tkinter.messagebox as messagebox

# Configuração de cores
COR_FUNDO = "#000000"
COR_BOTAO = "#0000FF"
COR_TEXTO = "#FFFFFF"
COR_LISTA = "#333333"

# Cria a janela principal
janela = tk.Tk()
janela.title("Gerenciador de Arquivos")
janela.geometry("700x650")
janela.configure(bg=COR_FUNDO)
janela.protocol("WM_DELETE_WINDOW", lambda: mostrar_mensagem_e_sair())

# Inicializa as variáveis globais
globals.inicializar_variaveis(janela)

# Variável para armazenar o observer do diretório
observer_atual = None

# Frame para os botões de filtro
frame_filtros = None

def filtrar_conteudo(caminho, tipo):
    lista_conteudo.delete(0, tk.END)
    conteudo = listar_conteudo(caminho)
    
    if tipo == "Todos":
        for item in conteudo:
            lista_conteudo.insert(tk.END, item)
    elif tipo == "Pastas":
        for item in conteudo:
            if os.path.isdir(os.path.join(caminho, item)):
                lista_conteudo.insert(tk.END, item)
    elif tipo == "Arquivos":
        for item in conteudo:
            if os.path.isfile(os.path.join(caminho, item)):
                lista_conteudo.insert(tk.END, item)
    elif tipo == "Imagens":
        extensoes_imagem = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        for item in conteudo:
            if os.path.isfile(os.path.join(caminho, item)) and os.path.splitext(item)[1].lower() in extensoes_imagem:
                lista_conteudo.insert(tk.END, item)
    elif tipo == "Vídeos":
        extensoes_video = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
        for item in conteudo:
            if os.path.isfile(os.path.join(caminho, item)) and os.path.splitext(item)[1].lower() in extensoes_video:
                lista_conteudo.insert(tk.END, item)

def atualizar_lista(caminho):
    global observer_atual
    
    # Para o monitoramento anterior se existir
    if observer_atual:
        parar_monitoramento(observer_atual)
    
    # Atualiza a lista
    filtrar_conteudo(caminho, globals.filtro_atual.get())
    
    # Inicia o monitoramento do novo diretório
    if caminho and os.path.isdir(caminho):
        observer_atual = iniciar_monitoramento(caminho, lambda: atualizar_lista(caminho))

def mostrar_filtros():
    global frame_filtros
    if frame_filtros is None:
        frame_filtros = tk.Frame(janela, bg=COR_FUNDO)
        frame_filtros.pack_forget()

        for valor in ["Todos", "Pastas", "Arquivos", "Imagens", "Vídeos"]:
            rb = tk.Radiobutton(frame_filtros, 
                              text=valor, 
                              variable=globals.filtro_atual, 
                              value=valor,
                              command=lambda v=valor: atualizar_lista(caminho_atual.get()),
                              bg=COR_FUNDO,
                              fg=COR_TEXTO,
                              selectcolor=COR_BOTAO,
                              activebackground=COR_BOTAO,
                              activeforeground=COR_TEXTO)
            rb.pack(side=tk.LEFT, padx=5)
        
        frame_filtros.pack(before=botao_sair, pady=5)

def selecionar_disco_e_mostrar_filtros():
    selecionar_disco()
    mostrar_filtros()

def mostrar_mensagem_e_sair():
    # Para o monitoramento antes de fechar
    if observer_atual:
        parar_monitoramento(observer_atual)
    messagebox.showinfo("Agradecimento", "Obrigado por nos executar!")
    janela.destroy()

# Interface do usuário
usuario_windows = os.getenv("USERNAME")
tk.Label(janela, text=f"Usuario logado: {usuario_windows}", font=("Arial", 10, "bold"), bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=5)

frame_discos = tk.Frame(janela, bg=COR_FUNDO)
frame_discos.pack(pady=10)

discos_var = tk.StringVar()
discos_var.set("Selecione um disco")
discos = listar_discos()

menu_discos = tk.OptionMenu(frame_discos, discos_var, *discos)
menu_discos.config(bg=COR_BOTAO, fg="white", activebackground=COR_BOTAO, activeforeground="white")
menu_discos["menu"].config(bg=COR_BOTAO, fg="white")
menu_discos.pack(pady=5)

tk.Frame(janela, height=20, bg=COR_FUNDO).pack()

frame_botoes = tk.Frame(janela, bg=COR_FUNDO)
frame_botoes.pack(pady=7)

tk.Button(frame_botoes, text="Abrir Disco", command=selecionar_disco_e_mostrar_filtros, bg=COR_BOTAO, fg="white").pack(side=tk.LEFT, padx=7)
tk.Button(frame_botoes, text="Histórico", command=exibir_historico, bg=COR_BOTAO, fg="white").pack(side=tk.LEFT, padx=7)
tk.Button(frame_botoes, text="Voltar", command=lambda: [voltar_diretorio(), atualizar_lista(caminho_atual.get())], bg=COR_BOTAO, fg="white").pack(side=tk.LEFT, padx=7)

caminho_atual = tk.StringVar()
tk.Label(janela, textvariable=caminho_atual, bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=5)

lista_conteudo = tk.Listbox(janela, width=80, height=20, bg=COR_LISTA, fg=COR_TEXTO)
lista_conteudo.pack(pady=10)
lista_conteudo.bind("<<ListboxSelect>>", selecionar_item)

botao_sair = tk.Button(janela, text="Sair", command=mostrar_mensagem_e_sair, bg="#FF5252", fg="white")
botao_sair.pack(pady=10)

janela.mainloop() 