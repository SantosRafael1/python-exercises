#Program to play some music... <3

from pygame import mixer
import time

mixer.init()
mixer.music.load("/home/amnesia/Music/music.mp3")
mixer.music.play()

while mixer.music.get_busy(): #wait the music finish to stop to play.
    time.sleep(1)