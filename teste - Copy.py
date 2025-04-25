# # Importar bibliotecas necessárias

# # Função para mover um arquivo
# def mover_arquivo(caminho_arquivo):
#     # Função interna para confirmar o movimento
#     def confirmar_movimento():
#         destino = entrada_destino.get()  # Obtém o caminho de destino inserido pelo usuário
#         if destino:
#             try:
#                 shutil.move(caminho_arquivo, destino)  # Move o arquivo para o destino
#                 registrar_operacao(caminho_arquivo, "Mover")  # Registra a operação
#                 messagebox.showinfo("Sucesso", "Arquivo movido com sucesso.")  # Exibe mensagem de sucesso
#                 janela_destino.destroy()  # Fecha a janela de destino
#             except Exception as e:
#                 messagebox.showerror("Erro", f"Erro ao mover o arquivo: {e}")  # Exibe mensagem de erro

#     # Criar uma nova janela para o usuário inserir o destino
#     janela_destino = tk.Toplevel(janela)
#     janela_destino.title("Selecionar Destino")  # Título da janela
#     janela_destino.geometry("400x150")  # Tamanho da janela

#     # Adicionar widgets para entrada do destino e botão de confirmação
#     tk.Label(janela_destino, text="Digite o caminho do destino:").pack(pady=10)
#     entrada_destino = tk.Entry(janela_destino, width=50)  # Campo de entrada para o destino
#     entrada_destino.pack(pady=5)
#     tk.Button(janela_destino, text="Confirmar", command=confirmar_movimento).pack(pady=10)

# # Função para excluir um arquivo
# def excluir_arquivo(caminho_arquivo):
#     # Exibe uma mensagem de confirmação para o usuário
#     confirmacao = messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o arquivo '{caminho_arquivo}'?")
#         except Exception as e:
#             messagebox.showerror("Erro", f"Erro ao excluir o arquivo: {e}")

# # Pilha para armazenar os caminhos visitados
# caminhos_visitados = []

# # Navegar por diretórios
# def navegar_diretorios(caminho):
#     if caminho_atual.get():
#         caminhos_visitados.append(caminho_atual.get())  # Salva o caminho atual antes de navegar
#     conteudo = listar_conteudo(caminho)
#     lista_conteudo.delete(0, tk.END)
#     for item in conteudo:
#         lista_conteudo.insert(tk.END, os.path.join(caminho, item))
#     caminho_atual.set(caminho)
#     registrar_operacao(caminho, "Navegar")

# # Voltar para o diretório anterior
# def voltar_diretorio():
#     if caminhos_visitados:
#         caminho_anterior = caminhos_visitados.pop()  # Recupera o último caminho visitado
#         navegar_diretorios(caminho_anterior)
#     else:
#         messagebox.showinfo("Aviso", "Não há diretórios anteriores para voltar.")

# # Selecionar um item na lista
# def selecionar_item(event):
#     try:
#         selecionado = lista_conteudo.get(lista_conteudo.curselection())
#         if os.path.isdir(selecionado):
#             navegar_diretorios(selecionado)
#         elif os.path.isfile(selecionado):
#             menu_arquivo(selecionado)
#     except tk.TclError:
#         pass

# # Menu de opções para um arquivo
# def menu_arquivo(caminho_arquivo):
#     janela_menu = tk.Toplevel(janela)
#     janela_menu.title("Menu de Arquivo")
#     janela_menu.geometry("300x200")

#     tk.Label(janela_menu, text=f"Arquivo: {os.path.basename(caminho_arquivo)}").pack(pady=10)
#     tk.Button(janela_menu, text="Abrir", command=lambda: abrir_arquivo(caminho_arquivo)).pack(fill=tk.X, padx=10, pady=5)
#     tk.Button(janela_menu, text="Copiar", command=lambda: copiar_arquivo(caminho_arquivo)).pack(fill=tk.X, padx=10, pady=5)
#     tk.Button(janela_menu, text="Mover", command=lambda: mover_arquivo(caminho_arquivo)).pack(fill=tk.X, padx=10, pady=5)
#     tk.Button(janela_menu, text="Excluir", command=lambda: excluir_arquivo(caminho_arquivo)).pack(fill=tk.X, padx=10, pady=5)
#     tk.Button(janela_menu, text="Fechar", command=janela_menu.destroy).pack(fill=tk.X, padx=10, pady=5)

# # Selecionar um disco
# def selecionar_disco():
#     disco = discos_var.get()
#     if disco:
#         navegar_diretorios(disco)

# # Configuração da janela principal
# janela = tk.Tk()
# janela.title("Gerenciador de Arquivos")
# janela.geometry("600x400")

# # Obter o nome do usuário do Windows
# usuario_windows = os.getenv("USERNAME")

# # Exibir o nome do usuário
# tk.Label(janela, text=f"Usuário logado: {usuario_windows}", font=("Arial", 10, "bold")).pack(pady=5)

# # Dropdown para selecionar discos
# discos_var = tk.StringVar()
# discos_var.set("Selecione um disco")
# discos = listar_discos()
# tk.OptionMenu(janela, discos_var, *discos).pack(pady=10)

# # Botão para navegar no disco selecionado
# tk.Button(janela, text="Abrir Disco", command=selecionar_disco).pack(pady=5)

# # Botão para voltar ao diretório anterior
# tk.Button(janela, text="Voltar", command=voltar_diretorio).pack(pady=5)

# # Caminho atual
# caminho_atual = tk.StringVar()
# tk.Label(janela, textvariable=caminho_atual).pack(pady=5)

# # Lista de conteúdo do diretório
# lista_conteudo = tk.Listbox(janela, width=80, height=20)
# lista_conteudo.pack(pady=10)
# lista_conteudo.bind("<<ListboxSelect>>", selecionar_item)

# # Botão para sair
# tk.Button(janela, text="Sair", command=janela.quit).pack(pady=10)

# # Iniciar a interface
# janela.mainloop()