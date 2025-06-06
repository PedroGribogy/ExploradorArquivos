# Monitorar mudanças no diretório

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class DiretorioHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_any_event(self, event):
        # Ignora eventos temporários e arquivos ocultos
        if event.src_path.endswith('~') or os.path.basename(event.src_path).startswith('.'):
            return
        
        # Atualiza a interface quando houver mudanças
        self.callback()

def iniciar_monitoramento(caminho, callback):
    """Inicia o monitoramento do diretório"""
    event_handler = DiretorioHandler(callback)
    observer = Observer()
    observer.schedule(event_handler, caminho, recursive=False)
    observer.start()
    return observer

def parar_monitoramento(observer):
    """Para o monitoramento do diretório"""
    if observer:
        observer.stop()
        observer.join() 