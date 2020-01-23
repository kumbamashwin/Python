# 1st method

lang = "perl,unix,hadoop,scala,spark,ruby,go"
strcheck = lang.find("python")

if strcheck == -1 :
    print("Not existing")
else:
    print("Existing")


# 2nd method
lang = "perl,unix,hadoop,scala,spark,ruby,go"
if 'python' in lang:
    print("existing")    
else:
    print("not existing")
    