# Selecionar um disco

def selecionar_disco():
    from windows.janela_principal import discos_var, caminho_atual, atualizar_lista
    from database.banco import registrar_operacao
    import globals
    
    disco = discos_var.get()
    if disco:
        caminho_atual.set(disco)
        globals.filtro_atual.set("Todos")
        atualizar_lista(disco)
        registrar_operacao(disco, "Abrir Disco") 