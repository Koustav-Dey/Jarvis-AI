import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

number_list = [0,1,2]

rand=random.choice(number_list)
random=int(rand)


engine = pyttsx3.init('sapi5')  #voice engine
voices = engine.getProperty('voices')   #get voice
# print(voices[4].id)
engine.setProperty('voice', voices[0].id) # set voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Night Sir")

    speak("Hello Sir. I am jarvis. Your Assistant. How Can I help u Sir ")


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e :
        # print(e)
        print("Say that again please.....")
        speak("Say that again please.....")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query :
            speak("Searching Wikipedia .... please wait ...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(f"\n Result is :{result}")
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'close youtube ' in query:
            webbrowser.close("youtube.com")

        elif 'hello jarvis' in query:
            speak("Hello Sir")

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random]) )

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Darknight\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'who are you' in query:
            speak("I am jarvis. Your Assistant. Just A Rather Very Intelligent System.")

        elif 'facebook ' in query:
            webbrowser.open("facebook.com")
        
        elif 'google ' in query:
            webbrowser.open("google.com")
       
        elif 'twitter ' in query:
            webbrowser.open("twitter.com")
        
        elif 'exit' in query:
            exit(0)

        
        