# Estilos comuns para todas as janelas

# Cores
COR_FUNDO = "#121212"  # Preto profundo
COR_BOTAO = "#BB86FC"  # Roxo Material Design
COR_TEXTO = "#FFFFFF"  # Branco
COR_LISTA = "#1F1F1F"  # Preto mais claro
COR_BOTAO_HOVER = "#9B4DFF"  # Roxo mais escuro
COR_VERMELHO = "#CF6679"  # Rosa Material Design
COR_BORDA = "#2D2D2D"  # Cinza para bordas
COR_ENTRADA = "#1F1F1F"  # Preto mais claro
COR_TITULO = "#03DAC6"  # Ciano Material Design

# Estilos de fonte
FONTE_TITULO = ("Segoe UI", 16, "bold")
FONTE_TEXTO = ("Segoe UI", 12)
FONTE_BOTAO = ("Segoe UI", 11, "bold")

# Estilos de botão
ESTILO_BOTAO = {
    "font": FONTE_BOTAO,
    "bg": COR_BOTAO,
    "fg": "#000000",  # Texto preto para melhor contraste
    "activebackground": COR_BOTAO_HOVER,
    "activeforeground": "#000000",
    "relief": "flat",
    "borderwidth": 0,
    "padx": 25,
    "pady": 10,
    "cursor": "hand2",
    "highlightthickness": 0,
    "width": 15
}

# Estilos de botão vermelho (para ações de exclusão/cancelamento)
ESTILO_BOTAO_VERMELHO = {
    **ESTILO_BOTAO,
    "bg": COR_VERMELHO,
    "activebackground": "#B00020",  # Vermelho mais escuro
    "fg": "#FFFFFF"  # Texto branco para melhor contraste
}

# Estilos de entrada de texto
ESTILO_ENTRADA = {
    "font": FONTE_TEXTO,
    "bg": COR_ENTRADA,
    "fg": COR_TEXTO,
    "insertbackground": COR_TEXTO,
    "relief": "flat",
    "borderwidth": 0,
    "highlightthickness": 1,
    "highlightbackground": COR_BOTAO,
    "highlightcolor": COR_BOTAO,
    "padx": 15,
    "pady": 8
}

# Estilos de label
ESTILO_LABEL = {
    "font": FONTE_TEXTO,
    "bg": COR_FUNDO,
    "fg": COR_TEXTO,
    "padx": 5,
    "pady": 2
}

# Estilos de título
ESTILO_TITULO = {
    "font": FONTE_TITULO,
    "bg": COR_FUNDO,
    "fg": COR_TITULO,
    "padx": 5,
    "pady": 5
}

# Configuração padrão de janela
def configurar_janela(janela, titulo, tamanho="450x300"):
    janela.title(titulo)
    janela.geometry(tamanho)
    janela.configure(bg=COR_FUNDO)
    # Centraliza a janela na tela
    try:
        janela.eval('tk::PlaceWindow . center')
    except AttributeError:
        # Centraliza manualmente se não for a janela principal
        janela.update_idletasks()
        largura = janela.winfo_width()
        altura = janela.winfo_height()
        x = (janela.winfo_screenwidth() // 2) - (largura // 2)
        y = (janela.winfo_screenheight() // 2) - (altura // 2)
        janela.geometry(f"{tamanho}+{x}+{y}")
    # Torna a janela modal (bloqueia interação com a janela principal)
    janela.transient(janela.master)
    janela.grab_set()
    # Adiciona padding e remove borda da janela
    janela.configure(padx=30, pady=30)
    janela.overrideredirect(False)
    # Adiciona sombra à janela
    janela.attributes('-alpha', 0.98)

# Função para criar frame de botões
def criar_frame_botoes(janela):
    frame = tk.Frame(janela, bg=COR_FUNDO)
    frame.pack(fill="x", pady=(25, 0))
    return frame 