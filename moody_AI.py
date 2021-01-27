#Harsha Narula
import time
import os
import playsound
import speech_recognition as sr
#import pyttsx3
from gtts import gTTS
import random
import pygame

#test
#last time
#made some changes to check
#lets see now what happens

#trying from different directory


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
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command)
    except sr.UnknownValueError:
        print("voice not clear")
            
    return command


#speak("hello illuminati. how are you feeling today?")
name = "illuminati"

my_dir = os.getcwd()


#songs directory
#good_path = "C:/Users/rijul/output/moody_AI/"
#bad_path = "C:/Users/rijul/output/moody_AI/"
#stress_path = "C:/Users/rijul/output/moody_AI/"
#motivation_path = "C:/Users/rijul/output/moody_AI/"

good_mp3 = [os.path.join(my_dir, f) for f in os.listdir(my_dir) if f.endswith('good.mp3')]
bad_mp3 = [os.path.join(my_dir, f) for f in os.listdir(my_dir) if f.endswith('sad.mp3')]
#stress_mp3 = [os.path.join(my_dir, f) for f in os.listdir(my_dir) if f.endswith('stress.mp3')]
motivation_mp3 = [os.path.join(my_dir, f) for f in os.listdir(my_dir) if f.endswith('motiv.mp3')]

random_good = random.choice(good_mp3)
random_bad = random.choice(bad_mp3)
#random_stress = random.choice(stress_mp3)
random_motivation = random.choice(motivation_mp3)

pygame.mixer.init()


speak("okay, "+name+" , say hello Google to activate me")

wake = "hello google"
temp = 0
numGood = 0
numBad = 0
numStress = 0
numMotivated = 0


while True:
    text=get_audio().lower()

    GOOD_STRS = ["good","happy","lucky","great"]
    BAD_STRS = ["bad","sad","depressed"]
    #STRESS_STRS = ["tensed","stressed"]
    MOTIVATION_STRS = ["motivated","motivating"]

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
                numGood=1
                break
        if numGood==1:
            break

        for bad in BAD_STRS:
            if bad in comm:
                speak("let me cheer you up by playing a wonderful song!")
                numBad=1
                break
        if numBad==1:
            break
        '''        
        for stress in STRESS_STRS:
            if stress in comm:
                speak("dont feel low. I will play something to uplift your mind.")
                numStress=1
                break
        if numStress==1:
            break
        '''   
        for motivation in MOTIVATION_STRS:
            if motivation in comm:
                speak("here you go sir!")
                numMotivated=1
                break
        if numMotivated==1:
            break    

if numGood==1:
    pygame.mixer.music.load(random_good)
    pygame.mixer.music.play()    

elif numBad==1:
    pygame.mixer.music.load(random_bad)
    pygame.mixer.music.play()    
   
elif numMotivated==1:
    pygame.mixer.music.load(random_motivation)
    pygame.mixer.music.play()    

while temp == 0:
    continue
                
        



        

        









