import cv2

# Inicializa a webcam (0 é o índice padrão da câmera do notebook)
cap = cv2.VideoCapture(0)

print("Pressione 'q' na janela do vídeo para fechar.")

while True:
    # Captura frame por frame
    ret, frame = cap.read()
    
    # Se não conseguir ler o frame, para o loop
    if not ret:
        print("Erro: Não foi possível acessar a webcam.")
        break
        
    # Exibe o frame em uma janela chamada 'IrisAssist - Webcam'
    cv2.imshow('IrisAssist - Webcam', frame)
    
    # Aguarda 1 milissegundo e verifica se a tecla 'q' foi pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas abertas
cap.release()
cv2.destroyAllWindows()
