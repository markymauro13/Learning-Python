
# open("employees.txt", "w")
# open("employees.txt", "a")
# open("employees.txt", "r+")

employee_file = open("employees.txt", "r")

#print(employee_file.read())
for i in employee_file.readlines():
    print(i)
#print(employee_file.readlines()[1])


employee_file.close()
