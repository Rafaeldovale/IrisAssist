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
def calcular_posicao(x_centro, largura_img):
    if x_centro < largura_img / 3:
        return "à esquerda"
    elif x_centro > (largura_img * 2) / 3:
        return "à direita"
    else:
        return "à frente"


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
            # Agora pegamos também o x_centro (primeiro valor)
            x_centro, _, w, h = box.xywh.squeeze()
            area_objeto = float(w * h)
            proporcao = area_objeto / area_total

            # 1. Ignora objetos muito distantes (menos de 1.5% da tela)
            if proporcao < 0.015:
                continue

            classe_id = int(box.cls)
            nome_ingles = model.names[classe_id]
            
            if nome_ingles in TRADUCAO:
                posicao = calcular_posicao(float(x_centro), largura_img)
                nome_pt = TRADUCAO[nome_ingles]
                
                # 2. Verifica se o objeto ocupa mais de 25% da tela (risco de colisão)
                                # 2. Alerta curto e direto (sem erro de gênero e rápido na voz)
                if proporcao > 0.50:
                    alerta_completo = f"Cuidado, {nome_pt} {posicao}"
                else:
                    alerta_completo = f"{nome_pt} {posicao}"

                    
                objetos_detectados.add(alerta_completo)



    return list(objetos_detectados), frame_anotado
