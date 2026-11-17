import cv2
from ultralytics import YOLO

# 1. Carrega o modelo leve
model = YOLO("yolov8n.pt")

# 2. Captura apenas 1 foto rápida da webcam
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

# 3. Roda a detecção nesse único frame
if ret:
    results = model(frame)
    for result in results:
        result.save(filename="resultado_teste.jpg")
        print("Sucesso! Imagem analisada e salva como resultado_teste.jpg")
else:
    print("Erro ao capturar imagem da webcam.")
