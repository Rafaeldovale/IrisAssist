import time
import cv2
from voice import falar_assincrono
from detector import detectar_objetos

cap = cv2.VideoCapture(0)
falar_assincrono("Sistema Iris Assist iniciado.")

contador_frames = 0
PULAR_FRAMES = 30
MAX_FRAMES = 450

ultimo_frame_anotado = None
ultimo_alerta = ""
tempo_ultimo_alerta = 0
INTERVALO_REPETICAO = 5.0  # Só repete o mesmo objeto após 5 segundos

while contador_frames < MAX_FRAMES:
    ret, frame = cap.read()
    if not ret:
        break

    contador_frames += 1

    if contador_frames % PULAR_FRAMES == 0:
        objetos, ultimo_frame_anotado = detectar_objetos(frame)
        
        if objetos:
            texto_alerta = ", ".join(objetos) + " à frente"
            agora = time.time()
            
            # Fala se o objeto mudou OU se já passaram 5 segundos desde o último aviso
            if texto_alerta != ultimo_alerta or (agora - tempo_ultimo_alerta) > INTERVALO_REPETICAO:
                print(f"[Detecção]: {texto_alerta}")
                falar_assincrono(texto_alerta)
                ultimo_alerta = texto_alerta
                tempo_ultimo_alerta = agora

    tela = ultimo_frame_anotado if ultimo_frame_anotado is not None else frame
    cv2.imshow("IrisAssist - Tempo Real", tela)
    
    tecla = cv2.waitKey(1) & 0xFF
    if tecla in [ord('q'), ord('Q')] or cv2.getWindowProperty("IrisAssist - Tempo Real", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
print("Sistema encerrado com segurança.")
