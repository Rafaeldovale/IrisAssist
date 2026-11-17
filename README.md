# IrisAssist - Sistema Assistivo com IA

Um sistema assistivo para deficientes visuais inspirado nos óculos inteligentes da Meta. O software utiliza 
a webcam para detectar objetos em tempo real e emitir alertas por voz localmente.

## 🚀 Status do Projeto
- [x] Estrutura inicial de pastas criada.
- [x] Ambiente virtual (.venv) configurado no Windows Nativo.
- [x] Teste de captura da webcam com OpenCV homologado com sucesso.
- [x] Integração com modelo YOLOv8 Nano (Ultralytics) validada em frame estático.
- [x] Módulo de áudio offline (Text-to-Speech) testado e homologado.
- [ ] Integração em tempo real com otimização de frames e áudio assíncrono.

## 🛠️ Tecnologias e Especificações do Ambiente
- **SO:** Windows Nativo (Acesso direto à Webcam)
- **Linguagem:** Python 3.12+
- **Hardware Alvo:** Processador Intel Celeron / 16GB RAM
- **Principais Bibliotecas:** OpenCV (v5.0.0+), PyTorch (v2.5.1), Ultralytics (YOLOv8n), pyttsx3

## 📊 Métricas de Benchmark (Hardware Local)
- **Inferência Estática (YOLOv8n):** ~969ms por frame (resolução 480x640 em CPU).
