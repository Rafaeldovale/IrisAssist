from ultralytics import YOLO
from config import (
    CONFIANCA_MINIMA,
    AREA_MINIMA_TELA,
    AREA_URGENCIA_TELA,
    TRADUCAO_OBJETOS
)

model = YOLO("yolov8n.pt")

def calcular_posicao(x_centro, largura_img):
    if x_centro < largura_img / 3:
        return "à esquerda"
    elif x_centro > (largura_img * 2) / 3:
        return "à direita"
    else:
        return "à frente"

def detectar_objetos(frame):
    results = model(frame, verbose=False, conf=CONFIANCA_MINIMA, imgsz=640)
    objetos_detectados = set()

    altura_img, largura_img, _ = frame.shape
    area_total = altura_img * largura_img
    frame_anotado = frame

    for result in results:
        frame_anotado = result.plot()
        for box in result.boxes:
            x_centro, _, w, h = box.xywh.squeeze()
            area_objeto = float(w * h)
            proporcao = area_objeto / area_total

            if proporcao < AREA_MINIMA_TELA:
                continue

            classe_id = int(box.cls)
            nome_ingles = model.names[classe_id]
            
            if nome_ingles in TRADUCAO_OBJETOS:
                posicao = calcular_posicao(float(x_centro), largura_img)
                nome_pt = TRADUCAO_OBJETOS[nome_ingles]
                
                if proporcao > AREA_URGENCIA_TELA:
                    alerta_completo = f"Cuidado, {nome_pt} {posicao}"
                else:
                    alerta_completo = f"{nome_pt} {posicao}"
                    
                objetos_detectados.add(alerta_completo)

    return list(objetos_detectados), frame_anotado
