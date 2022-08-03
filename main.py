import keyboard
import time
from playsound import playsound

while True:
    if keyboard.read_key()=='w':
        playsound("1.wav")
        time.sleep(0.02)
    if keyboard.read_key()=='a':
        playsound("2.wav")
        time.sleep(0.02)
    if keyboard.read_key()=='s':
        playsound("3.wav")
        time.sleep(0.02)
    if keyboard.read_key()=='d':
        playsound("4.wav")
        time.sleep(0.02)