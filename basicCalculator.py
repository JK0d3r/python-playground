num1 = float(input("Enter your first number here: "))
op = input("Enter the operation you want to do here: ")
num2 = float(input("Enter your second number here: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operation, please use \"+\", \"-\", \"*\", or \"/\".")