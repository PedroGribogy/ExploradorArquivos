#        GERENCIADOR
#            DE
#         ARQUIVOS

import os
import sys

# Adiciona o diretório raiz ao PYTHONPATH
diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
if diretorio_raiz not in sys.path:
    sys.path.append(diretorio_raiz)

# Importa as funções principais
from navigation.listar_discos import listar_discos
from functions.abrir_arquivo import abrir_arquivo
from functions.copiar_arquivo import copiar_arquivo
from functions.mover_arquivo import mover_arquivo
from functions.excluir_arquivo import excluir_arquivo
from navigation.navegar_diretorios import navegar_diretorios
from navigation.voltar_diretorio import voltar_diretorio
from navigation.selecionar_item import selecionar_item
from windows.menu import menu_arquivo
from navigation.selecionar_disco import selecionar_disco

# Inicia a interface principal
from windows.janela_principal import janela

# Inicia o loop principal da interface
janela.mainloop()



