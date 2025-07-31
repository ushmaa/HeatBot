import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import subprocess
import pywhatkit 


# 🔊 Setup voice engine
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# 🎤 Take command from mic
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        return query.lower()

    except Exception as e:
        print("Couldn't recognize:", e)
        speak("Sorry, I didn't catch that. Please say again.")
        return "none"




# start
speak("Hello, I am Jarvis. How can I help you?")
query = take_command()



if 'wikipedia' in query:
    speak("Searching Wikipedia...")
    try:
        result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
        speak(result)
    except Exception as e:
        print(" Wikipedia failed:", e)
        speak("Sorry, I couldn't find anything.")

elif 'open youtube' in query:
    speak("Opening YouTube")
    try:
        subprocess.Popen(["cmd", "/c", "start", "https://youtube.com"])
    except Exception as e:
        print(" Could not open YouTube:", e)
        speak("I tried, but I couldn’t open YouTube.")

elif 'time' in query:
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time}")

# elif 'play' in query and 'youtube' in query:
#     song = query.replace("play", "").replace("on youtube", "").strip()
#     speak(f"Playing {song} on YouTube")
#     try:
#         pywhatkit.playonyt(song)
#     except Exception as e:
#         speak("Sorry, I couldn't play that song.")
#         print("[ERROR] YouTube playback failed:", e)

else:
    print(f"[No match] Query was: {query}")
    speak("Sorry, I didn't understand that.")


   
