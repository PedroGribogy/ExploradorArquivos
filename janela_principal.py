# Configuaracao da janela principal

import tkinter as tk # Permite criar um interface grafica
import os # Permite acesso ao sistema operacional
from listar_discos import listar_discos # Importa a funcao para listar os discos
import selecionar_disco # Importa o módulo selecionar_disco
from voltar_diretorio import voltar_diretorio # Importa a funcao para voltar ao diretorio anterior
from selecionar_item import selecionar_item # Importa a funcao para selecionar item do diretorio
from listar_conteudo import listar_conteudo # Importa a funcao para listar o conteudo
import globals # Importa o módulo globals
from historico import exibir_historico # Importa a funcao para exibir o historico

# Configuração de cores
COR_FUNDO = "#000000"  # Preto
COR_BOTAO = "#4CAF50"  # Verde
COR_TEXTO = "#FFFFFF"  # Branco
COR_LISTA = "#333333"  # Cinza escuro

# Cria a janela principal antes de qualquer outra operação
janela = tk.Tk()
janela.title("Gerenciador de Arquivos")
janela.geometry("700x650")
janela.configure(bg=COR_FUNDO)

# Inicializa as variáveis globais
globals.inicializar_variaveis(janela)

# Frame para os botões de filtro (definido globalmente para poder mostrar/esconder)
frame_filtros = None

def filtrar_conteudo(caminho, tipo):
    """Filtra o conteúdo do diretório baseado no tipo selecionado"""
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
    """Atualiza a lista com o filtro atual"""
    filtrar_conteudo(caminho, globals.filtro_atual.get())

def mostrar_filtros():
    """Mostra os botões de filtro"""
    global frame_filtros
    if frame_filtros is None:
        frame_filtros = tk.Frame(janela, bg=COR_FUNDO)
        frame_filtros.pack_forget()  # Não mostra ainda

        # Botões de filtro com cores invertidas quando selecionados
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
        
        # Reposiciona o frame de filtros antes do botão Sair
        frame_filtros.pack(before=botao_sair, pady=5)

def selecionar_disco_e_mostrar_filtros():
    """Função que combina a seleção do disco e exibição dos filtros"""
    selecionar_disco.selecionar_disco()  # Chama a função do módulo
    mostrar_filtros()

# Obter o nome do usuario do Windows
usuario_windows = os.getenv("USERNAME") # Chama a funcao que verifica qual o usuario do Windows esta conectado
tk.Label(janela, text=f"Usuario logado: {usuario_windows}", font=("Arial", 10, "bold"), bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=5) # Mostra na janela qual usuario esta logado

# Frame para o seletor de discos
frame_discos = tk.Frame(janela, bg=COR_FUNDO)
frame_discos.pack(pady=10)

# Dropdown para selecionar os discos
discos_var = tk.StringVar() # Cria a opca de selecionar os discos
discos_var.set("Selecione um disco") # Abre um selecao, para o usuario escolher qual disco deseja
discos = listar_discos() # Verifica quais os discos existentes

# Estiliza o menu dropdown
menu_discos = tk.OptionMenu(frame_discos, discos_var, *discos)
menu_discos.config(bg=COR_BOTAO, fg="white", activebackground=COR_BOTAO, activeforeground="white")
menu_discos["menu"].config(bg=COR_BOTAO, fg="white")
menu_discos.pack(pady=5)

# Adiciona um espaçador
tk.Frame(janela, height=20, bg=COR_FUNDO).pack()

# Frame para os botões principais
frame_botoes = tk.Frame(janela, bg=COR_FUNDO)
frame_botoes.pack(pady=7)

# Botões principais lado a lado
tk.Button(frame_botoes, text="Abrir Disco", command=selecionar_disco_e_mostrar_filtros, bg=COR_BOTAO, fg="white").pack(side=tk.LEFT, padx=7)
tk.Button(frame_botoes, text="Histórico", command=exibir_historico, bg=COR_BOTAO, fg="white").pack(side=tk.LEFT, padx=7)
tk.Button(frame_botoes, text="Voltar", command=lambda: [voltar_diretorio(), atualizar_lista(caminho_atual.get())], bg=COR_BOTAO, fg="white").pack(side=tk.LEFT, padx=7)

# Caminho atual
caminho_atual = tk.StringVar() # Cria a opcao de ver os caminhos
tk.Label(janela, textvariable=caminho_atual, bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=5) # Cria uma janela com os caminhos 

# Lista dos conteudos do diretorio
lista_conteudo = tk.Listbox(janela, width=80, height=20, bg=COR_LISTA, fg=COR_TEXTO) # Janela que lista o conteudo do diretorio
lista_conteudo.pack(pady=10) # Posiciona o widget
lista_conteudo.bind("<<ListboxSelect>>", selecionar_item) # Chama a funcao quando o usuario selecionar algum item

# Botao para sair (definido como variável global para referência)
botao_sair = tk.Button(janela, text="Sair", command=janela.quit, bg="#FF5252", fg="white")
botao_sair.pack(pady=10) # Cria um botao para sair da execucao

# Iniciar a interface
janela.mainloop() # Mantem a janela aberta para as interacoes do usuario