import time
import os
import playsound
import speech_recognition as sr
#import pyttsx3
from gtts import gTTS
import random
import pygame

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

#songs directory
path = "C:/Users/rijul/Desktop/sample_songs/"
all_mp3 = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]
randomfile = random.choice(all_mp3)
pygame.mixer.init()
pygame.mixer.music.load(randomfile)

#speak("okay, "+name+" , say hello amanda to activate me")

wake = "hello amanda"
num = 0

while True:
    text=get_audio().lower()

    GOOD_STRS = ["good","happy","lucky","great"]
    BAD_STRS = ["bad","sad","depressed"]
    STRESS_STRS = ["tensed","stressed"]

    if text.count(wake) > 0:
        speak("hello, "+name+" ,how can i help you?")
        try:
            comm = get_audio().lower()
        except :
            speak("sorry i didn't hear you")
            continue

        for good in GOOD_STRS:
            if good in comm:
                speak("awesome! i have the perfect song in store for you")
                pygame.mixer.music.play()
                

        for bad in BAD_STRS:
            if bad in comm:
                speak("let me cheer you up by playing a wonderful song!")
                pygame.mixer.music.play()

                
        for stress in STRESS_STRS:
            if stress in comm:
                speak("dont feel low. I will play something to uplift your mind.")
                pygame.mixer.music.play()
                
        



        

        









