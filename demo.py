atup = (10,20,30,40,56)
#atup[0] = 2000

print("****** converting tuple to list ****")
## converting to the list
alist = list(atup)
# making the changes
alist[0] = 10000
# reconverting back to tuple
atup = tuple(alist)
print(atup)


# capture input
name = input("Enter any name :")
print("You entered  :", name)

alist = [10,20,30]

print(max(alist))
print(min(alist))
print(id(alist))

name = 'python'
print(type(name))
print(isinstance(name,str))