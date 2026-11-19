import cv2
from ultralytics import YOLO

# Carrega o modelo apenas UMA vez na memória quando o arquivo é importado
model = YOLO("yolov8n.pt")

# Dicionário básico de tradução (Dataset COCO -> Português)
TRADUCAO = {
    "person": "pessoa",
    "chair": "cadeira",
    "cup": "copo",
    "bottle": "garrafa",
    "cell phone": "celular",
    "laptop": "notebook",
    "car": "carro",
    "dog": "cachorro"
}

def detectar_objetos(frame):
    # verbose=False evita poluir o terminal com logs a cada segundo
    # conf=0.5 exige no mínimo 50% de certeza do modelo
    results = model(frame, verbose=False, conf=0.5)
    objetos_detectados = set()  # 'set' evita repetir "pessoa, pessoa" se houver duas

    for result in results:
        for box in result.boxes:
            classe_id = int(box.cls[0])
            nome_ingles = model.names[classe_id]
            
            # Traduz se estiver no dicionário, senão ignora por enquanto
            if nome_ingles in TRADUCAO:
                objetos_detectados.add(TRADUCAO[nome_ingles])

    return list(objetos_detectados)