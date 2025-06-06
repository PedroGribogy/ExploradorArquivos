# Listar conteúdo de um diretório

import os

def listar_conteudo(caminho):
    """Lista o conteúdo de um diretório"""
    try:
        # Lista todos os itens no diretório
        itens = os.listdir(caminho)
        
        # Filtra apenas arquivos e diretórios (ignora links simbólicos, etc)
        itens = [item for item in itens if os.path.isdir(os.path.join(caminho, item)) or os.path.isfile(os.path.join(caminho, item))]
        
        # Ordena os itens (diretórios primeiro, depois arquivos)
        itens.sort(key=lambda x: (not os.path.isdir(os.path.join(caminho, x)), x.lower()))
        
        return itens
    except Exception as e:
        print(f"Erro ao listar conteúdo: {e}")
        return [] 