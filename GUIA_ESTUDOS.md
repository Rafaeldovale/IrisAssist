# 📘 Diário de Bordo & Guia Técnico — IrisAssist

Este guia resume as decisões de arquitetura, bibliotecas e conceitos de Machine Learning aplicados neste projeto, estruturado para consulta rápida e entrevistas técnicas.

---

## 🏗️ 1. Arquitetura Modular (`src/`)

* **`src/camera.py` (Captura):** Módulo isolado de teste de hardware usando OpenCV. Garante a leitura frame a frame e a liberação correta da memória (`cap.release()`).
* **`src/detector.py` (Visão Computacional):** Carrega o modelo **YOLOv8 Nano** uma única vez na RAM. Converte os tensores matemáticos (`box.xywh`) em métricas espaciais reais:
  * **Filtro de Área (`< 1.5%`):** Descarta objetos distantes ao fundo para evitar alucinações.
  * **Direção Espacial:** Divide a largura da imagem em 3 terços (esquerda, à frente, direita).
  * **Estimativa de Proximidade (`> 50%`):** Dispara alerta prioritário quando o obstáculo ocupa mais da metade do campo de visão.
* **`src/voice.py` (Síntese de Voz Assíncrona):** Usa `pyttsx3` (motor nativo SAPI5 do Windows) rodando em uma `Thread` paralela isolada com `pythoncom.CoInitialize()`, evitando que o vídeo congele enquanto o sistema fala.
* **`src/main.py` (Orquestrador):** Conecta visão e áudio em tempo real aplicando:
  * **Frame Skipping (`PULAR_FRAMES = 30`):** Analisa 1 quadro por segundo para não sobrecarregar o processador Intel Celeron.
  * **Cooldown de Alerta (`5s`):** Evita repetição cansativa (*fadiga de alerta*) se a cena não mudou.
  * **Fail-Safe (`MAX_FRAMES`):** Encerramento automático de segurança.

---

## 🛠️ 2. Por que escolhemos essas Bibliotecas?
* **OpenCV (`opencv-python`):** Padrão da indústria para captura e manipulação de matrizes de imagem em tempo real.
* **Ultralytics (`YOLOv8n`):** Modelo estado-da-arte de detecção de objetos. Escolhemos a variante **Nano (`n`)** (~6MB) por ser otimizada para inferência em CPU sem placa de vídeo dedicada (GPU).
* **PyTorch (`torch`):** Motor matemático de Deep Learning que executa os pesos da rede neural por baixo do YOLO.
* **pyttsx3 + pywin32:** Text-to-Speech 100% offline, garantindo privacidade, zero custo de API e funcionamento sem internet.
