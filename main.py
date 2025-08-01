import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import subprocess
import pywhatkit 
import time
import datetime


# Setup voice engine
engine = pyttsx3.init()


def read_notes():
    file_name = "notes.txt"
    try:
        with open(file_name, "r") as file:
            notes = file.readlines()
            if notes:
                speak("Here are your notes:")
                for line in notes:
                    speak(line.strip())
            else:
                speak("Your notes file is empty.")
    except FileNotFoundError:
        speak("I couldn’t find any saved notes yet.")


  

def save_note(note_text):
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = "notes.txt"
    with open(file_name, "a") as file:
        file.write(f"[{time_stamp}] {note_text}\n")
    speak("Note saved successfully.")


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

    elif 'note' in query or 'remember' in query:
        speak("What should I write down?")
        note = take_command()
        if note != "none":
           save_note(note)
        else:
           speak("I didn’t catch that. Note not saved.")


    elif 'read' in query or 'show notes' in query or 'what did i tell you' in query:
        read_notes()
      
        

    else:
        print(f"[No match] Query was: {query}")
        speak("Sorry, I didn't understand that.")
