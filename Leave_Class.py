import time
import keyboard

print("\nCurrent time is",time.strftime("%H:%M:%S", time.localtime()))

def take_time_input():
    time_to_leave=input(str("\nEnter time to leave the class. for example:- 14:05:00  --->   "))
    
    if time_to_leave > time.strftime("%H:%M:%S", time.localtime()):
    
        return time_to_leave

    else:
        print("\nInput time is exceeded by current time or is the wrong format")
        take_time_input()
    

time_to_leave=take_time_input()

while True :

    if  time.strftime("%H:%M:%S", time.localtime()) > time_to_leave:
        keyboard.press_and_release('ctrl', 'shift','B')
        print("\nPressed ctrl, shift, B. Meeting exited.\n")
        break

    time.sleep(10)