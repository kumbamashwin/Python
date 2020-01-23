
lcount =0
dcount =0
wcount =0

string = input("Enter any string:")

for char in string:
    if char.isalpha():
        lcount = lcount + 1
    elif char.isdigit():
        dcount = dcount + 1
    elif char.isspace():
        wcount = wcount + 1
        
print("Letters      ",lcount)
print("Digits       ",dcount)
print("White spaces ",wcount)