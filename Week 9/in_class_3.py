"""
Alarm Clock

Create a program where the user can enter an 
amount of minutes. 

The program should then wait for that time period.

While waiting, the program should print a random
number (from 1 to 5) of `Z` every second.

at the end of said time, the program should beep
a sound at 1000 hz for 5 seconds.
"""

import time
import random
import winsound

def timer():
    minutes = int(input('Enter the number of minutes: '))

    seconds = minutes * 60

    interval_s = 1

    for x in range(int(seconds)):
        for i in range(random.randint(1,5)):
            print("Z", end= "")
        print()
        time.sleep(interval_s)

    print("WAKE UP!!!")
    winsound.Beep(1000,5000)

timer()