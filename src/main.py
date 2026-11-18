import cv2
from voice import falar_assincrono


# Inicializa a câmera e avisa por voz
cap = cv2.VideoCapture(0)
falar_assincrono("Sistema Iris Assist iniciado.")

contador_frame = 0
PULAR_FRAME = 30 # Analisa 1 frame a cada 30 segundos

while True:

    ret, frame = cap.read()
    if not ret:
        break

    contador_frame += 1

    # verifica se chegou a hora de analisar o frame
    if contador_frame % PULAR_FRAME == 0:
        print(f"Frame {contador_frame}: Hora de chamar o YOLO!")

    cv2.imshow("IrisAssist - Tempo Real", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    """# Aceita 'q' minúsculo ou 'Q' maiúsculo, ou fechar no 'X' da janela
    tecla = cv2.waitKey(1) & 0xFF
    if tecla in [ord('q'), ord('Q')] or cv2.getWindowProperty("IrisAssist - Tempo Real", cv2.WND_PROP_VISIBLE) < 1:
        break"""

cap.release()
cv2.destroyAllWindows()