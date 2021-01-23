import time
import os
import playsound
import speech_recognition as sr
#import pyttsx3
import subprocess
import webbrowser
import tkinter
import requests
import datetime
import wolframalpha
from gtts import gTTS

'''
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',170)
    engine.setProperty('volume',2.0)    
    engine.say(text)
    engine.runAndWait()
'''

def speak(text):
    tts = gTTS(text = text, lang = 'en-us')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    #try:
    command = r.recognize_google(audio)
    print('You said: ' + command)
    #except sr.UnknownValueError:
    #print("voice not clear")
        
        
    return command


speak("hello illuminati. how are you feeling today?")
name = "illuminati"

#speak("okay, "+name+" , say hello amanda to activate me")

wake = "hello amanda"
num = 0

while True:
    text=get_audio().lower()

    GOOD_STRS = ["good","happy","lucky","great"]
    BAD_STRS = ["bad","sad","depressed"]
    STRESS_STR = ["tensed","stressed"]

    if text.count(wake) > 0:
        speak("hello, "+name+" ,how can i help you?")
        try:
            comm = get_audio().lower()
        except :
            speak("sorry i didn't hear you")
            continue

        for good in GOOD_STRS:
            if words in comm:
                speak("awesome! i have the perfect song in store for you")
                continue

        if "nothing" in comm:
            speak("okay. just say hello amanda to activate me")
            continue
            
        elif "chrome" in comm:
            speak("opening chrome")
            chrome()

        elif "mozilla" in comm:
            speak("opening mozilla")
            mozilla()

        elif "change my name" in comm:
            speak("what would you want me to set your new name?")

            try:
                name = get_audio().lower()
            except :
                speak("sorry i didn't hear you")
                continue

            speak("okay, "+name+" ,i have changed your name in my database")

        elif "youtube" in comm:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "google" in comm:
            speak("opening google")
            webbrowser.open("google.com")

        elif "wikipedia" in comm:
            speak("opening wikipedia")
            webbrowser.open("wikipedia.com")

        elif "facebook" in comm:
            speak("opening facebook")
            webbrowser.open("facebook.com")

        elif "weather" in comm:
            speak("scanning your area with satellites all around the world")
            weather()

        elif "time" and "now" in comm:
            abhi = datetime.datetime.now()
            print(abhi)
            speak("the time has been displayed on the screen!")
            
        elif "shutdown" or "switch off" in comm:          
            option = get_audio().lower()
            subprocess.call('shutdown / p /f')

        elif "pdf" and "reader" in comm:
            speak("opening p,d,f reader")
            pdf()

        elif "what is" in query or "who is" in query: 
            client = wolframalpha.Client("API_ID") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results")
        
        speak("just say hello amanda to reactivate me")

        

        







import os
import random
import pygame

path = "C:/Users/rijul/Desktop/sample_songs/"
all_mp3 = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]

randomfile = random.choice(all_mp3)

pygame.mixer.init()
pygame.mixer.music.load(randomfile)
pygame.mixer.music.play()
