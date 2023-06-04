# import all sub modules of TKINTER Module
from tkinter import *
import datetime
import time
import winsound
#Input Parameter from user as Time
def alarm(set_alarm_timer):
    while True:
        time.sleep(2)
        #This will show current time (DD:MM:YYYY, HH:MM:SS)
        current_time=datetime.datetime.now()
        now=current_time.strftime("%H:%M:%S")
        date=current_time.strftime("%d/%m/%Y")
        print("Today Date is :",date,"Current Time is :",now)
        if now ==set_alarm_timer:
            print("ALARM : Time to Wake Up")
            winsound.PlaySound(r"C:\Users\hashp\Downloads\sound.mp3",winsound.SND_ASYNC)
            #Checking Time
#Creating UI Screen so these function
def actual_time():
    set_alarm_timer=f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
#GUI
clock=Tk()
clock.title("Alarm CLock Project in Python")
clock.iconbitmap(r"C:\Users\hashp\Downloads\clock.ico")
clock.geometry("400x200")
time_format = Label(clock,text="Enter the time 24 hour format!!",fg="red", bg="black",font="Arial").place(x=60,y=120)
addTime=Label(clock,text="Hour, Min, Sec", font=60).place(x=110)

setYourAlarm=Label(clock,text="When to Wake You Up", fg="blue",relief="solid",font=("Arial",7,"bold")).place(x=0,y=29)

#Define Varaible
hour=StringVar()
min=StringVar()
sec=StringVar()
#mapping Variables
hourTime=Entry(clock,textvariable=hour, bg="pink", width=15).place(x=110,y=30)
minTime=Entry(clock,textvariable=min, bg="pink", width=15).place(x=150,y=30)
secTime=Entry(clock,textvariable=sec, bg="pink", width=15).place(x=200,y=30)
                   #Submitting  Button
submit=Button(clock,text ="Set Alarm:", fg="red", bg="blue", width=10, command=actual_time).place(x=110,y=70)
clock.mainloop()
