import random
import time
wonderBoyAllowance=10
newCape=20
print("That new cape sure is shiny. I wonder if you can afford it...")
time.sleep(1.5)
if wonderBoyAllowance<newCape:
    print("You are broke. Maybe if you ask nicely Wonder Dad will give you a raise...")
if bool(random.getrandbits(1)):
    wonderBoyAllowance=25
    print("raise given")
    time.sleep(1.5)
    print("Congrats! You now have a real cape!")
else:
    print("raise rejected")
    time.sleep(1.5)
    print("Looks like you'll have to keep wearing that towel as a cape...")