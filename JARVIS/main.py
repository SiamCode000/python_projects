import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def proccessCommand(c):
    if("open google" in c.lower()):
        webbrowser.open("https://www.google.com/")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://www.youtube.com/")
    elif("open facebook" in c.lower()):
        webbrowser.open("https://www.facebook.com/")
    elif(c.lower().startswith("play")):
        try:
            song_input = c.lower().replace("play", "").strip()
            for title in musiclibrary.music:
                if title.lower() == song_input:
                    link = musiclibrary.music[title]
                    print(f"Playing: {title} → {link}")
                    webbrowser.open(link)
                    speak(f"Playing {title}")
                    return
            speak("Sorry, I couldn't find that song.")
        except Exception as e:
            print(f"Error: {e}")

def speak(text):
    engine.say(text)
    engine.runAndWait()

if (__name__ == "__main__"):
    speak("Initializing Jarvis....")
    while True:
        recognizer = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = recognizer.listen(source,timeout=2,phrase_time_limit=9)
                recognizer.adjust_for_ambient_noise(source, duration=1)
            word = recognizer.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yes")
                with sr.Microphone() as source:
                    print("Jarvis Activated..!")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    proccessCommand(command)
        except Exception as e:
            print("error; {0}".format(e))

