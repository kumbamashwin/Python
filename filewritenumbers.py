


## write operation
fw = open("numbers.txt","w")
for val in range(1,10):
    fw.write(str(val) + "\n")
fw.close()