import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import sys

# Função para falar
def falar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Troque para voices[1] se quiser outra voz
    engine.say(texto)
    engine.runAndWait()
    engine.stop()

# Função para ouvir
def ouvir():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        falar("Desculpe, não entendi.")
        print("Desculpe, não entendi.")
        return ""
    except sr.RequestError:
        falar("Erro na conexão com o serviço de reconhecimento.")
        print("Erro na conexão com o serviço de reconhecimento.")
        return ""

# Função principal
def executar_comando(comando):
    if "que horas são" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        falar(f"Agora são {hora}")
        print(f"Agora são {hora}")

    elif "pesquisar" in comando:
        termo = comando.replace("pesquisar", "").strip()
        if termo:
            falar(f"Pesquisando por {termo}")
            print(f"Pesquisando por {termo}")
            wikipedia.set_lang("pt")
            try:
                resumo = wikipedia.summary(termo, sentences=2)
                falar(resumo)
                print(resumo)
            except wikipedia.exceptions.DisambiguationError:
                falar("Termo ambíguo, seja mais específico.")
                print("Termo ambíguo, seja mais específico.")
            except wikipedia.exceptions.PageError:
                falar("Não encontrei nada sobre isso.")
                print("Não encontrei nada sobre isso.")
        else:
            falar("Você não disse o que deseja pesquisar.")
            print("Você não disse o que deseja pesquisar.")

    elif "tocar" in comando:
        musica = comando.replace("tocar", "").strip()
        if musica:
            falar(f"Tocando {musica}")
            print(f"Tocando {musica}")
            pywhatkit.playonyt(musica)
        else:
            falar("Você não disse o que deseja tocar.")
            print("Você não disse o que deseja tocar.")

    elif "sair" in comando:
        falar("Até logo!")
        print("Até logo!")
        sys.exit()

    else:
        falar("Não entendi o comando.")
        print("Não entendi o comando.")

# Loop principal
try:
    while True:
        comando = ouvir()
        if comando:
            executar_comando(comando)
except KeyboardInterrupt:
    falar("Encerrando assistente...")
    sys.exit()
