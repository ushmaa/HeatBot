import pyttsx3  
import speech_recognition as sr  
import datetime  
import os
import wikipedia  

engine = pyttsx3.init() 


def speak(text):
    engine.say(text)       
    engine.runAndWait() 

speak("Hello, how are you?")



def take_command():
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  
        audio = r.listen(source)  

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # audio → text
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query







speak("Hello, I am Jarvis. How can I help you?")
query = take_command()  # user ka command suno

if 'wikipedia' in query.lower():
    speak('Searching Wikipedia...')
    try:
        result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
        speak(result)
    except Exception as e:
        print("[ERROR] Wikipedia lookup failed:", e)
        speak("Sorry, I couldn't find that on Wikipedia.")


elif 'open youtube' in query:
    speak("Opening YouTube")
    os.system('start "" "https://youtube.com"')

elif 'time' in query:
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time}")

else:
    speak("Sorry, I didn't understand that.")


 
