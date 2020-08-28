# Helathy Programmer
# 9am - 5pm
# Water -  water.mp3(3.5 litres ) (for closing type Drank)
#1 glaases in 32 min and all 14 glassess
# Eyes -   eyes.mp3 (Done) every 30 minutes (Eydone)
# Physical Activity -  every 45 min.__doc__ (Exdone)
# Rules:-
# pygame module to play audio
print("*****************************")
print("*****Healthy Programmer*****")
print("*****************************")
print("Timmings is 9am - 5pm")

from pygame import mixer
import datetime
import time
import schedule
import sys

start_local_time = time.asctime(time.localtime(time.time()))
start_time = time.time()


def water():
    if (True):
        # To playing Water Alert!!!!
        mixer.init()
        mixer.music.load("water.mp3")
        mixer.music.play(-1)
        a = input("Enter drank\nif You Drank the 250ml water: ")
        if (a == 'drank'):
            # To written the time in the particular file
            f = open("exercise_healthy_programmer.txt","a")
            f.write("\n*************************\n")
            f.write("You Drink Water at : \n")
            t = time.asctime(time.localtime(time.time()))
            f.write(t)
            f.write("\n")
            # To stop the Water Alert!!!
            mixer.music.stop()

def eyes():
    if(True):
        # TO playing Eyes Alert!!!!
        mixer.init()
        mixer.music.load("eyes.mp3")
        mixer.music.play(-1)
        a = input("Enter done\nif You wash the eyes: ")
        if (a == 'done'):
            # To written the time in the particular file
            f = open("exercise_healthy_programmer.txt", "a")
            f.write("\n*************************\n")
            f.write("You Wash Eyes at : \n")
            t = time.asctime(time.localtime(time.time()))
            f.write(t)
            f.write("\n")
            # To stop the Eyes Alert!!!
            mixer.music.stop()

def exercise():
    if(True):
        # To start the Exercise Alert
        mixer.init()
        mixer.music.load("exercise.mp3")
        mixer.music.play(-1)
        a = input("Enter done\nif You Done the Exercise: ")
        if(a == 'done'):
            # To written the time in the particular file
            f = open("exercise_healthy_programmer.txt", "a")
            f.write("\n*************************\n")
            f.write("You Done Exercise at : \n")
            t = time.asctime(time.localtime(time.time()))
            f.write(t)
            f.write("\n")
            # To stop the Exercise Alert!!!
            mixer.music.stop()

def start():
    schedule.every(30).minutes.do(water)
    schedule.every(35).minutes.do(eyes)
    schedule.every(45).minutes.do(exercise)

#
# def start():
#     schedule.every(15).seconds.do(water)
#     schedule.every(25).seconds.do(eyes)
#     schedule.every(20).seconds.do(exercise)


def end():
    sys.exit()
schedule.every().day.at("09:00").do(start)
schedule.every().day.at("17:00").do(end)

while 1:
    schedule.run_pending()
    time.sleep(1)
