import pyttsx3

# Inicializa o motor de voz nativo do Windows
engine = pyttsx3.init()

# Ajusta a velocidade da fala (padrão costuma ser ~200, 175 fica mais claro)
engine.setProperty('rate', 175)

def falar(texto):
    print(f"[IrisAssist Voz]: {texto}")
    engine.say(texto)
    engine.runAndWait()

# Teste isolado
if __name__ == "__main__":
    falar("Sistema Iris Assist iniciado. Alerta de teste: pessoa à frente.")
