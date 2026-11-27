# Configurações de Câmera e Performance (Otimizado para Celeron)
PULAR_FRAMES = 30
MAX_FRAMES = 450

# Configurações de Voz e Alerta
VELOCIDADE_VOZ = 175
INTERVALO_REPETICAO = 5.0  # Segundos antes de repetir o mesmo alerta

# Parâmetros Geométricos e de Confiança do YOLO
CONFIANCA_MINIMA = 0.35
AREA_MINIMA_TELA = 0.015   # 1.5% da tela (ignora ruídos distantes)
AREA_URGENCIA_TELA = 0.50  # 50% da tela (dispara alerta "Cuidado")

# Dicionário de Tradução (COCO Dataset -> Português)
TRADUCAO_OBJETOS = {
    "person": "pessoa",
    "chair": "cadeira",
    "cup": "copo",
    "bowl": "tigela",
    "bottle": "garrafa",
    "cell phone": "celular",
    "laptop": "notebook",
    "book": "livro",
    "remote": "controle",
    "backpack": "mochila",
    "handbag": "bolsa",
    "keyboard": "teclado",
    "mouse": "mouse"
}
