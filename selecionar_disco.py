# Selecionar um disco

# Funcao selecionar_disco

def selecionar_disco(): # Cria a funcao selecionar_disco
    from janela_principal import discos_var, caminho_atual, atualizar_lista, janela
    from banco import registrar_operacao # Importa a função para registrar operações
    import globals
    
    disco = discos_var.get() # Verifica se ha algum disco selecionado
    if disco: # Se tiver algum disco selecionado ira executar
        caminho_atual.set(disco) # Atualiza o caminho atual
        globals.filtro_atual.set("Todos")  # Reseta o filtro para "Todos"
        atualizar_lista(disco) # Atualiza a lista com o conteúdo do disco
        registrar_operacao(disco, "Abrir Disco") # Registra a abertura do disco
        
# Fim selecionar_disco
        