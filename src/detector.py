from ultralytics import YOLO

model = YOLO("yolov8n.pt")

TRADUCAO = {
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

def detectar_objetos(frame):
    results = model(frame, verbose=False, conf=0.35)
    objetos_detectados = set()

    for result in results:
        for box in result.boxes:
            classe_id = int(box.cls)
            nome_ingles = model.names[classe_id]
            
            if nome_ingles in TRADUCAO:
                objetos_detectados.add(TRADUCAO[nome_ingles])

    # results[0].plot() devolve a imagem original com os quadrados desenhados
    frame_anotado = results[0].plot()
    return list(objetos_detectados), frame_anotado
