#FRANK ASSISTANT CODE
import pywhatkit
import speech_recognition as sr
import pyttsx3


#Frank reconoce tu voz
name = 'frank'
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#Frank habla
def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


#Frank escucha
def listen():

    try:    
        with sr.Microphone() as source:
            print('listener...')
            audio = r.listen(source)
            text = r.recognize_google(audio, language='en-US')
            text = text.lower()
            if name in text:
                text = text.replace(name, '')

    except:
        pass
    return text


#funcion principal
def run_frank():
    talk('Hi, i am frank')
    text = listen()
    
    print(text)

    if 'reproduce' in text:
        music = text.replace('reproduce', '')
        print('reproduciendo...')
        talk('reproduciendo ' + music)
        pywhatkit.playonyt(music)
    else:
        talk('you are number one!')


run_frank()
