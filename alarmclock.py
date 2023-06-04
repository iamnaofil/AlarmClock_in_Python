import datetime
import time
import winsound
def set_alarm():
    alarm_time=input("Enter the time for the Alarm (HH:MM AM/PM): ")
    try:
        alarm_time = datetime.datetime.strptime(alarm_time, "%I:%M %p")
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Alarm set for {alarm_time.strftime('%I:%M %p')}.")
        while current_time != alarm_time.strftime("%I:%M %p"):
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            time.sleep(1)
        play_alarm_sound()
        print("Alarm is going off!")
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM.")

def play_alarm_sound():
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)

set_alarm()
    
