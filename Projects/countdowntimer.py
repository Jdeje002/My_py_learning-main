import time
import datetime

#create timer function

def countdown(s,m,h):
    total_seconds = s + (m * 60) + (h * 3600)
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("\n")
    print("Time's up!")

h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter seconds: "))

countdown(s,m,h)



