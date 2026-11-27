# 👁️ IrisAssist — Sistema Assistivo com IA

Um sistema assistivo de baixo custo inspirado nos óculos inteligentes da Meta, desenvolvido para auxiliar pessoas com deficiência visual. O software utiliza a webcam do notebook para detectar objetos em tempo real, calcular sua posição espacial e emitir alertas por voz localmente (100% offline).

---

## ✨ Funcionalidades Principais
- **Detecção em Tempo Real:** Identificação simultânea de objetos e pessoas usando **YOLOv8 Nano**.
- **Orientação Espacial:** Cálculo geométrico da posição do obstáculo no campo de visão (*à esquerda*, *à frente* ou *à direita*).
- **Nível de Urgência (Proximidade):** Estimativa de risco baseada na proporção da área ocupada na tela, disparando alertas prioritários (*"Cuidado..."*) quando um objeto está muito próximo.
- **Filtro de Ruído de Fundo:** Descarte inteligente de objetos muito pequenos/distantes para evitar alucinações e excesso de informação.
- **Áudio Assíncrono Offline:** Síntese de voz nativa sem congelar o fluxo de vídeo e com memória de curto prazo (*cooldown*) para evitar repetição cansativa.

---

## 🚀 Status do Projeto (v1.0 Concluída)
- [x] Estrutura inicial de pastas criada.
- [x] Ambiente virtual (.venv) configurado no Windows Nativo.
- [x] Teste de captura da webcam com OpenCV homologado com sucesso.
- [x] Integração com modelo YOLOv8 Nano (Ultralytics) validada em frame estático.
- [x] Módulo de áudio offline (Text-to-Speech) testado e homologado.
- [x] Integração em tempo real com otimização de frames, direção espacial e áudio assíncrono.

---

## 🏗️ Arquitetura do Projeto

```text
IrisAssist/
├── src/
│   ├── camera.py      # Módulo isolado de captura e teste de hardware (OpenCV)
│   ├── detector.py    # Inferência YOLOv8n, tradução e cálculos espaciais/proximidade
│   ├── voice.py       # Motor Text-to-Speech assíncrono (Threading + COM Windows)
│   └── main.py        # Orquestrador em tempo real com Frame Skipping e Fail-Safe
├── GUIA_ESTUDOS.md    # Diário de bordo técnico e decisões de arquitetura
├── requirements.txt   # Dependências exatas do ambiente
└── README.md          # Documentação principal
```

---

## 🛠️ Tecnologias e Especificações do Ambiente
- **SO:** Windows Nativo (Acesso direto à Webcam)
- **Linguagem:** Python 3.12+
- **Hardware Alvo:** Processador Intel Celeron / 16GB RAM (Foco em Otimização)
- **Principais Bibliotecas:** OpenCV (v5.0.0+), PyTorch (v2.5.1), Ultralytics (YOLOv8n), pyttsx3, pywin32

## 📊 Métricas de Benchmark & Desafios Resolvidos
- **Inferência Estática (YOLOv8n):** ~969ms por frame (resolução 480x640 em CPU).
- **Otimização de Borda (*Edge AI*):** Implementação de *Frame Skipping* (análise a cada 30 frames) e carregamento único do modelo em RAM para manter o vídeo fluido no Intel Celeron.
- **Concorrência de Áudio no Windows:** Isolamento do `pyttsx3` (SAPI5) via `threading` + `pythoncom.CoInitialize()` para evitar travamento da janela do OpenCV.

---

## 💻 Como Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd IrisAssist
   ```

2. **Crie e ative o ambiente virtual (Windows):**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. **Instale as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Execute o sistema:**
   ```powershell
   python src/main.py
   ```
   *(Nota: Na primeira execução, o arquivo de pesos leve `yolov8n.pt` será baixado automaticamente).*
