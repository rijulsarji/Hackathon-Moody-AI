import os
import random
import pygame

path = "C:/Users/rijul/Desktop/sample_songs/"
all_mp3 = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]

randomfile = random.choice(all_mp3)

pygame.mixer.init()
pygame.mixer.music.load(randomfile)
pygame.mixer.music.play()
