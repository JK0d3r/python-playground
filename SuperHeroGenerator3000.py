# importing the random module to use for randomizing strings and numbers later
import random
from time import time
# Importing the time module to create a delay
import time
brains=0
braun=0
stamina=0
wisdom=0
power=0
constitution=0
dexterity=0
speed=0
answer=''
# Creating a list of possible super powers
superPowers=['Flying','Super Strength','Telepathy','Super Speed','Can Eat a Lot of Hot Dogs','Good At Skipping Rope']
# Creating lists of possible first and last names
superFirstName=['Wonder','Whatta','Rabid','Incredible','Astonishing','Decent','Stupendous','Above-average','That Guy','Improbably']
superLastName=['Boy','Man','Dingo','Beefcake','Girl','Woman','Guy','Hero','Max','Dream','Macho Man','Stallion']
#Introductory Text
print("Are you ready to create a super hero with the Super Hero Genereator 3000?")
# Ask the user a question and prompt them for an answer
# input() 'listens' to what they type on their keyboard
# We then use upper() to change the users answer to all uppercase letters
print("Enter Y for yes or N for no:")
answer=input()
answer=(answer.upper())
# While loop check for the answer "Y"
# This loop will continue while the value of answer IS NOT "Y"
# Only when the user types "Y" will the loop exit and the program continue
while answer!="Y":
    print("I'm sorry, but you have to enter Y to continue!")
    print("Enter Y for yes or N for no:")
    answer=input()
    answer=(answer.upper())
print("Great, let's get started!")
time.sleep(2)
print("Randomizing name...")
# Creating suspense using the time() function
for i in range(3):
    print("...........")
    time.sleep(3)
print("(I bet you can't stand the suspense!)")
print("")
time.sleep(2)
# Randomizing Super Hero name
# We do this by choosing one name from each name list
# And adding it to the variable superName
superName=random.choice(superFirstName)+ " " +random.choice(superLastName)
print("Your Super Hero Name is:")
print(superName)
print("")
time.sleep(3)
print("Now it's time to see what super power you have!")
time.sleep(2.5)
print("(generating super hero power...)")
# Creating dramatic effect again
for i in range(2):
    print("...........")
    time.sleep(3)
print("(nah...you wouldn't like THAT one...)")
for i in range(2):
    print("...........")
    time.sleep(3)
print("(almost there...)")
time.sleep(2)
# Randomly choosing super power from the superPowers list
# and assigning it to the variable power
power=random.choice(superPowers)
print("Your new super power is:")
time.sleep(2)
print(power)
print("")
time.sleep(3)
print("Last but not least, let's generate your stats!")
time.sleep(2)
print("Will you be super smart? Super strong? Super Good Looking?")
time.sleep(2)
print("Time to find out!")
# Creating dramatic effect and slowing the program down again
for i in range(3):
    print("...........")
    time.sleep(3)
# Randomly filling in each of the below variables with a new value
# The new values will range from 1-20
brains=random.randint(1,20)
braun=random.randint(1,20)
stamina=random.randint(1,20)
wisdom=random.randint(1,20)
constitution=random.randint(1,20)
dexterity=random.randint(1,20)
speed=random.randint(1,20)
# Printing out the statistics
print("Your new stats are:")
print("")
time.sleep(2)
print("Brains: ", brains)
time.sleep(2)
print("Braun: ", braun)
time.sleep(2)
print("Stamina: ", stamina)
time.sleep(2)
print("Wisdom: ", wisdom)
time.sleep(2)
print("Constitution: ", constitution)
time.sleep(2)
print("Dexterity: ", dexterity)
time.sleep(2)
print("Speed: ", speed)
print("")
time.sleep(2)
# Printing summary of hero
# Includes name, super power, and stats
print("Here is a summary of your new Super Hero!")
print("")
time.sleep(2)
print("Character Summary:")
print("")
print("")
time.sleep(2)
print("Super Hero Name: ", superName)
time.sleep(2)
print("Super Power: ", power)
print("")
time.sleep(2)
print("Brains: ", brains)
time.sleep(2)
print("Braun: ", braun)
time.sleep(2)
print("Stamina: ", stamina)
time.sleep(2)
print("Wisdom: ", wisdom)
time.sleep(2)
print("Constitution: ", constitution)
time.sleep(2)
print("Dexterity: ", dexterity)
time.sleep(2)
print("Speed: ", speed)
time.sleep(2)
print("Thank you for using the Super Hero Generator 3000!")
time.sleep(2)
print("Tell all your friends!")