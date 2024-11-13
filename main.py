#Dos pasos para instalar whisper
#1. pip install -U openai-whisper / git+https://github.com/openai/whisper.git
#2. choco install ffmpeg (para windows usando chocolatey)

import whisper #Transcriptor
from gtts import gTTS #Voz virtual
import speech_recognition as sr
import os
from langchain_community.llms import Ollama

llm = Ollama(model="mistral")


# import pyttsx3

recognizer = sr.Recognizer()

print("hola")

while True:
    try:
        with sr.Microphone() as mic:
            print("escuchando...")
            recognizer.adjust_for_ambient_noise(mic, duration= 0.5)
            audio = recognizer.listen(mic)

            with open('speech.wav', 'wb') as f:
                f.write(audio.get_wav_data())

            #Voz a Texto
            model = whisper.load_model("base")
            result = model.transcribe('speech.wav')
            print(result["text"])

            # #Texto a Voz
            print("procesando")
            text = llm.invoke(result["text"])
            language = 'es-us'
            speech = gTTS(text = text, lang = language, slow = False)
            speech.save("vozArtificial.mp3") #Guardar archivo
            os.system("start vozArtificial.mp3")
                
    except sr.UnknownValueError():
        recognizer = sr.Recognizer()
        continue
