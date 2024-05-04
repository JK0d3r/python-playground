# r means to just read a file, w is to change the file, a is to append, or add new things
# r+ means reading and writing

employee_file = open("employees.txt", "r")
# print(employee_file.readable())  <-- returns a boolean to check if it's readable or not
for employee in employee_file.readlines():
    print(employee)
employee_file.close()