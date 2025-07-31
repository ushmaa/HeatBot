import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import subprocess
import pywhatkit 
import time


# 🔊 Setup voice engine
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        time.sleep(1)
        r.adjust_for_ambient_noise(source, duration=0.5)  # 🔧 Important
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"[DEBUG] You said: {query}")
        return query.lower()

    except sr.UnknownValueError:
        print("Google Speech could not understand audio")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
    except Exception as e:
        print("Couldn't recognize:", e)

    speak("Sorry, I didn't catch that. Please say again.")
    return "none"


# start
speak("Hello, I am Jarvis. How can I help you?")


while True:
    query = take_command()

    if query == "none":
        continue

    if 'stop' in query or 'exit' in query:
        speak("Goodbye! See you later.")
        break

    elif 'wikipedia' in query:
        speak("Searching Wikipedia...")
        try:
            result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
            speak(result)
        except Exception as e:
            print("Wikipedia failed:", e)
            speak("Sorry, I couldn't find anything.")

    elif 'open youtube' in query:
        speak("Opening YouTube")
        try:
            subprocess.Popen(["cmd", "/c", "start", "https://youtube.com"])
        except Exception as e:
            print("Could not open YouTube:", e)
            speak("I tried, but I couldn’t open YouTube.")

    elif 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif 'play' in query and 'youtube' in query:
        song = query.replace("play", "").replace("on youtube", "").strip()
        speak(f"Playing {song} on YouTube")
        try:
            pywhatkit.playonyt(song)
        except Exception as e:
            speak("Sorry, I couldn't play that song.")
            print("[ERROR] YouTube playback failed:", e)

    else:
        print(f"[No match] Query was: {query}")
        speak("Sorry, I didn't understand that.")
