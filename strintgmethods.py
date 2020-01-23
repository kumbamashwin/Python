########### working with string methods #######

name = "python programming"
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.count('p'))  # display the count of p in string
print(name.replace('python','ruby'))
print(name.isupper())   # validating the string is upper or
print(name.center(30))  #
print(name.startswith("m"))
print(name.startswith("p"))
bname= "I love {} and {}"  ## string template
print(bname.format("unix","java"))
print(bname.format("scala","liux"))
cname = " python         "
print(cname.strip()) # strip will remove spaces
print(cname.lstrip())
print(cname.rstrip())
print("a".ljust(6))  # displaying from the left of 6 spaces
print("a".rjust(6))  # displaying from the left of 6 spaces
print(name)
 