import numpy as np

array = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print("Printing 2D Array")
print(array)

print("Choose random row from a 2D array")
randomRow = np.random.randint(3, size=1)
print(array[randomRow[0], :])

print("Random item from random row is")
print(np.random.choice(array[randomRow[0], :]))