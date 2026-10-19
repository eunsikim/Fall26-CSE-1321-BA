import time

def timer():
    minutes = int(input('Enter the number of minutes: '))

    seconds = minutes * 60

    interval_s = 1

    for x in range(int(seconds)):
        print(time.ctime(time.time()))
        time.sleep(interval_s)

    print("WAKE UP!!!")

timer()