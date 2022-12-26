wonderBoyAllowance=20
newCape=20
print("That new cape sure is shiny. I wonder if you can afford it...")
if wonderBoyAllowance>newCape:
    print("Congrats! You have enough to buy that new cape!")
    print("And it looks like you have some money left over.")
    print("How about getting a haircut? Your hair is covering your mask!")
elif wonderBoyAllowance==newCape:
    print("You have exactly enough money to purchase the cape!")
    print("No change for you!")
    print("Eh...and no tip for me I see...")
else:
    print("Looks like you'll have to keep wearing that towel as a cape...")
    print("Maybe if you ask nicely Wonder Dad will give you a raise...")