import cv2
from voice import falar_assincrono
from detector import detectar_objetos

cap = cv2.VideoCapture(0)
falar_assincrono("Sistema Iris Assist iniciado.")

contador_frames = 0
PULAR_FRAMES = 30
MAX_FRAMES = 450  # Aumentamos para ~15 segundos para dar tempo de testar vários objetos

while contador_frames < MAX_FRAMES:
    ret, frame = cap.read()
    if not ret:
        break

    contador_frames += 1

    # A cada 30 frames, envia a imagem atual para o YOLO analisar
    if contador_frames % PULAR_FRAMES == 0:
        objetos = detectar_objetos(frame)
        
        if objetos:
            texto_alerta = ", ".join(objetos) + " à frente"
            print(f"[Detecção]: {texto_alerta}")
            falar_assincrono(texto_alerta)

    cv2.imshow("IrisAssist - Tempo Real", frame)
    
    tecla = cv2.waitKey(1) & 0xFF
    if tecla in [ord('q'), ord('Q')] or cv2.getWindowProperty("IrisAssist - Tempo Real", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
print("Sistema encerrado com segurança.")
