from ast import Break
password=''
passwordAttempt=0
print("Welcome to Optimal Dad's Vault of Gadgets")
while password!="wonderboyiscool2018":
    print("Please enter your password to access some fun tech!")
    password=input()
    password=(password.lower())
    passwordAttempt=passwordAttempt+1
    if password=="wonderboyiscool2018":
        print("You entered the correct password:", password)
        print("Please take whatever gadgets you need!")
        print("Don't touch the Doom Canon though - that belongs to Optimal Dad!")
    elif passwordAttempt==3:
        print("Sorry, you are out of attempts")
        break
    