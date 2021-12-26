import imp
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import time

# define speaking
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def initial():
# Initialization...
    speak("Initializing Apollo..")
    print("Initializing Apollo..")
    speak("30%..")
    print("30%..")
    speak("45%..")
    print("45%..")
    speak("74%..")
    print("74%..")
    speak("100%\n Welcome To Apollo Ai")
    print("100%\n Welcome To Apollo Ai")

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Im Listening...')
        speak('What would you like me to do?')
        audio = r.listen(source)

    try :
        print('Recognizing...')
        speak('Recognizing...')
        query = r.recognize_google(audio, language='en-us')
        print(f' User said: {query}\n')
        speak(f' User said: {query}')

    except Exception as e:
        print('Please repeat that.')
        speak('Please repeat that.')
        query = None
    return query
    
# initial()
query = Command()



if 'wikipedia' in query.lower():
    print("Searching wikipedia...")
    speak("Searching wikipedia...")
    query = query.replace("wikipedia", '')
    results = wikipedia.summary(query, sentences= 2)
    print(f'\n {results} \n')
    speak(results)

elif 'open youtube' in query.lower():
    webbrowser.open('https://youtube.com')
    speak('Youtube is now open')
    print('Youtube is now open.')

elif 'open google' in query.lower():
    webbrowser.open('https://google.com')
    speak('Google is now open')
    print('Google is now open.')

elif 'play lo-fi' in query.lower():
    webbrowser.open('https://www.youtube.com/watch?v=mStI2VsCGhM&list=PLdUzWlLG9V3MAuZsEDROwPBLzDw1pC-RR')
    speak('playing lofi')
    print('playing lofi')

elif 'play lofi' in query.lower():
    webbrowser.open('https://www.youtube.com/watch?v=mStI2VsCGhM&list=PLdUzWlLG9V3MAuZsEDROwPBLzDw1pC-RR')
    speak('playing lofi')
    print('playing lofi')


elif 'time' in query.lower():
    strTime = datetime.datetime.now().strftime('%H:%M:%S')
    speak(f"The time is {strTime}")

elif 'open discord' in query.lower():
    Path1 = 'C:\\Users\\bobsf\\AppData\\Local\\DiscordPTB\\app-1.0.1010\\DiscordPTB.exe'
    os.startfile(Path1)

