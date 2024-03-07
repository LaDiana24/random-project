#import all necessary libraries to form the alarm clock

from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H-%M-%S")
        date = current_time.strftime("%d-%m-%Y")
        print("The date is:", date)
        print(now)
        if  now == set_alarm_timer:
            print("TIme to Wake Up")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)