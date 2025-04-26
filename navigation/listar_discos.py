# Listar discos disponiveis no sistema

import os

def listar_discos():
    """Lista todos os discos disponíveis no sistema"""
    return [f"{chr(d)}:\\" for d in range(65, 91) if os.path.exists(f"{chr(d)}:\\")] 