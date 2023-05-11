# https://www.fesliyanstudios.com/royalty-free-sound-efects-download/alarm-203

from playsound import playsound

import time

# ANSI Characters
CLEAR        = "\033[2J"
CLEAR_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
  
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
  
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 # 125/60 => 2
        seconds_left = time_left % 60 # 125 % 60 => 5

        print(f"{CLEAR_RETURN}Alarm will sound in {minutes_left:02d}:{seconds_left:02d}") # :02d will print 2 digits and pad zero

    playsound("alarm.mp3")

minutes = int(input("Enter the minutes to wait: "))
seconds = int(input("Enter the seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
