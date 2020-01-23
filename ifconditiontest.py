
############ if-else ###############
name = "python programming"

if len(name)> 5  and name.islower():
    print("exists")
else:
    print("doesnt exist")


#############  if-elif-elif-elif..... else #######
color = input("Enter any color :")

if color == "red":
    print("Red color")
elif color == "black"):
    print("Black color")
elif color == "green":
    print("green color")
else:
    print("Unknown color")

######  check the file extension ########
filename = "abc.py"

if filename.endswith(".py"):
    print("its python file")
elif filename.endswith(".java"):
    print("java file")
else:
    print("Unknown file")
        
