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

import winsound

def main():
    winsound.Beep(500, 2000)

if __name__ == "__main__":
    main()