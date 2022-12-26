import time
import AppKit
import os

print("Sinister Loop, I know you are in there!")
print("If you don't come out of the cafeteria freezer by the time I finish counting...")
print("You won't get any of that delicious stop-sign shaped pizza!")
print("Tell me how many seconds you want the timer for...")
i = int(input())
for x in range(1,i+1):
    print (x, "Mississippi")
    AppKit.NSBeep()
    time.sleep(.1)
print("I warned you! Now all the pizza belongs to Wonder Boy!")
os.system('say "I warned you! Now all the pizza belongs to Wonder Boy u fat dumdum!"')