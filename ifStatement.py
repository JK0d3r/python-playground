is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are tall, but not a male.")
else:
    print("You are neither male not tall.")