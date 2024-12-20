import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return ""

def speechtx(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        data1 = sptext().lower()
        
        if "your name" in data1:
            name = "My name is Atish"
            speechtx(name)
            
        elif "how old are you" in data1:
            age = "I am 20 years old"
            speechtx(age)
            
        elif "time" in data1:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speechtx(time)
            
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com")
            
        elif "replit" in data1:
            webbrowser.open("https://replit.com")
            
        elif "joke" in data1:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke_1)
            speechtx(joke_1)
            
        # Uncomment and correct the following block if needed
        # elif "photos" in data1:
        #     add = "C:\\Users\\nandi\\OneDrive\\Pictures"
        #     listphotos = os.listdir(add)
        #     print(listphotos)
        #     os.startfile(os.path.join(add, listphotos[0]))
                
        elif "exit" in data1:
            speechtx("Thank you")
            break
