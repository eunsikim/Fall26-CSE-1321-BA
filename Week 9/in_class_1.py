import time

def timer():
    minutes = int(input('Enter the number of minutes: '))

    for x in range(minutes):
        print(x)
        time.sleep(60)

    print("WAKE UP!!!")

timer()