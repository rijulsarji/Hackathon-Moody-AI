#                                    MOODY AI

#importing libraries
import time
import os
import playsound
import speech_recognition as sr
import pyttsx3
import random
from win32 import win32api
import pygame
import win32com
#using pyttsx3 engine for text-to-speech

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',170)
    engine.setProperty('volume',2.0)    
    engine.say(text)
    engine.runAndWait()

#converting audio to text

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nlistening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('\nYou said: ' + command)
    except sr.UnknownValueError:
        print("voice not clear")
            
    return command


#speak("hello there. how are you feeling today?")

name = "There" #name of the user

my_dir = os.getcwd() #to get current directory for the music files




#specifying directory for music files

good_mp3 = [os.path.join(my_dir, f) for f in os.listdir(my_dir) if f.endswith('good.mp3')]
bad_mp3 = [os.path.join(my_dir, f) for f in os.listdir(my_dir) if f.endswith('sad.mp3')]
#stress_mp3 = [os.path.join(my_dir, f) for f in os.listdir(my_dir) if f.endswith('stress.mp3')]
motivation_mp3 = [os.path.join(my_dir, f) for f in os.listdir(my_dir) if f.endswith('motiv.mp3')]


#randomising music files

random_good = random.choice(good_mp3)
random_bad = random.choice(bad_mp3)
random_stress = random.choice(stress_mp3)
random_motivation = random.choice(motivation_mp3)


#randomising choices other than music files

choices = [0,1,2]
random_recom = random.choice(choices)
numRecom=0


pygame.mixer.init() #initialise pygame.mixer module


speak("okay, "+name+" , say hello friend to activate me") #introductory message

wake = "hello friend" #wake command for the assistant


pygame.init() #initialise pygame module

temp = 0 #for creating an infinite loop


#for breaking the respective loops

numGood = 0
numBad = 0
numStress = 0
numMotivated = 0


#main loop starts

while temp==0:

    while True:


        text=get_audio().lower()


        #possible responses

        GOOD_STRS = ["good","happy","lucky","great"]
        BAD_STRS = ["bad","sad","depressed"]
        STRESS_STRS = ["tensed","stressed"]
        MOTIVATION_STRS = ["low","demotivated","motivated","high"]


        if text.count(wake) > 0:
            speak("hello, "+name+" ,how can i help you?")
            try:
                comm = get_audio().lower()
            except :
                speak("sorry i didn't hear you")
                continue

            #good mood starts
            
            for good in GOOD_STRS:
                if good in comm:
                    speak("awesome! i have the perfect song in store for you")
                    numGood=1
                    break

            if numGood==1:
                break

            
            #sad mood starts

            for bad in BAD_STRS:
                if bad in comm:
                    speak("let me cheer you up by playing a wonderful song!")
                    numBad=1
                    break
            if numBad==1:
                break


            #stress mood starts

                    
            for stress in STRESS_STRS:
                if stress in comm:
                    speak("dont feel low. I will play something to uplift your mind.")
                    numStress=1
                    break
            if numStress==1:
                break
               


            #motivation mood starts

            for motivation in MOTIVATION_STRS:
                if motivation in comm:
                    if random_recom == 0:
                        speak("here you go sir!")
                        numMotivated=1
                        break
                    else:
                        speak("i recommend watching rocky.")
                        numRecom==1
                        break
                
        if numMotivated==1 or numRecom==1:
            break 


    #conditions to play respective songs              

    if numGood==1:
        pygame.mixer.music.load(random_good)
        pygame.mixer.music.play()    

    elif numBad==1:
        pygame.mixer.music.load(random_bad)
        pygame.mixer.music.play()    
       
    elif numMotivated==1:
        pygame.mixer.music.load(random_motivation)
        pygame.mixer.music.play()    

    elif numStress==1:
        pygame.mixer.music.load(random_stress)
        pygame.mixer.music.play()    
    
    while temp == 0:
        keys=pygame.key.get_pressed()
        char=input()
        if char=="pause":
            pygame.mixer.music.pause()
        elif char=="play":
            pygame.mixer.music.unpause()
        elif char=="exit"or"Exit"or"EXIT":
            break
        else:
            continue
    
    #condition to exit the program

    break    



        

        









