# Proyect : Python Assistant
# Author : Fabricio Sebastian Davila
# Date : 23/01/2022

import pyttsx3
import pywhatkit
import speech_recognition as sr

name = "julio"
engine = pyttsx3.init()
voices = engine.getProperty("voices")
newVoiceRate = 145
engine.setProperty('rate', newVoiceRate)
engine.setProperty("voices", voices[2].id)


def talk(some_text):
    engine.say(some_text)
    engine.runAndWait()


def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            talk("¿Que necesitas?")
            listener.adjust_for_ambient_noise(source)
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
    except sr.UnknownValueError:
        print("No te entendí. Intenta nuevamente")
    return rec


def run_roboto():
    while True:
        try:
            rec = listen()
            print(rec)
        except UnboundLocalError:
            talk("No te entendí. Intenta nuevamente")
            continue
        if name in rec:
            rec = rec.replace(name, '').strip()
            print(rec)
            if 'reproduce' in rec:
                song = rec.replace('reproduce', '').strip()
                pywhatkit.playonyt(song)
                talk(f"Reproduciendo {song}")
        if 'salir' in rec:
            talk("Apagando asistente")
            return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_roboto()
