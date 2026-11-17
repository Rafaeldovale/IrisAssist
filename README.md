# IrisAssist - Sistema Assistivo com IA

Um sistema assistivo para deficientes visuais inspirado nos óculos inteligentes da Meta. O software utiliza a webcam para detectar objetos em tempo real e emitir alertas por voz localmente.


## 🚀 Status do Projeto
- [x] Estrutura inicial de pastas criada.
- [x] Ambiente virtual (.venv) configurado no Windows Nativo.
- [x] Teste de captura da webcam com OpenCV homologado com sucesso.
- [x] Integração com modelo YOLO (Ultralytics).
- [ ] Implementação de áudio assíncrono (Text-to-Speech).
- [ ] Integração em tempo real com otimização de frames (Frame Skipping).


## 🛠️ Tecnologias e Especificações do Ambiente
- **SO:** Windows Nativo (Acesso direto à Webcam)
- **Linguagem:** Python 3.12+
- **Hardware Alvo:** Processador Intel Celeron / 16GB RAM (Foco em Otimização)
- **Principais Bibliotecas:** OpenCV (v5.0.0+)


## 📊 Métricas de Benchmark (Hardware Local)
- **Inferência Estática (YOLOv8n):** ~969ms por frame (resolução 480x640 em CPU).