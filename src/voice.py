import threading
import pyttsx3
import pythoncom

esta_falando = False

def _tarefa_falar(texto):
    global esta_falando
    esta_falando = True
    # Inicializa o recurso de áudio do Windows para esta thread específica
    pythoncom.CoInitialize()
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 175)
        print(f"[IrisAssist Voz]: {texto}")
        engine.say(texto)
        engine.runAndWait()
    finally:
        # Libera o recurso do Windows e a trava
        pythoncom.CoUninitialize()
        esta_falando = False

def falar_assincrono(texto):
    if not esta_falando:
        thread = threading.Thread(target=_tarefa_falar, args=(texto,), daemon=True)
        thread.start()

if __name__ == "__main__":
    import time
    falar_assincrono("Testando voz em segundo plano.")
    print("O código principal CONTINUOU rodando sem esperar a voz terminar!")
    time.sleep(5)
