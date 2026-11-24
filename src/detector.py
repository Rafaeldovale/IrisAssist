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
    results = model(frame, verbose=False, conf=0.35, imgsz=640)
    objetos_detectados = set()

    altura_img, largura_img, _ = frame.shape
    area_total = altura_img * largura_img
    frame_anotado = frame

    for result in results:
        frame_anotado = result.plot()
        for box in result.boxes:
            # .squeeze() transforma [[x, y, w, h]] em [x, y, w, h]
            _, _, w, h = box.xywh.squeeze()
            area_objeto = float(w * h)

            # Ignora objetos pequenos ao fundo (menos de 5% da área da tela)
            if (area_objeto / area_total) < 0.05:
                continue

            classe_id = int(box.cls)
            nome_ingles = model.names[classe_id]
            
            if nome_ingles in TRADUCAO:
                objetos_detectados.add(TRADUCAO[nome_ingles])

    return list(objetos_detectados), frame_anotado
