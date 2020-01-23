adict = {"emp1":["raj",28] ,"emp2":["ram",34] ,"emp3":["rita",24]}


if 'emp2' in adict:
    print("emp2 exists")
else:
    print("doesn't exists")
    
    
## 2nd method
adict = {"emp1":["raj",28] ,"emp2":["ram",34] ,"emp3":["rita",24]}

getkeys = list(adict.keys())

if 'emp2' in getkeys:
    print ("exists")
else:
    print("not exists")
    
    ## 3rd menthod
adict = {"emp1":["raj",28] ,"emp2":["ram",34] ,"emp3":["rita",24]}

if adict.get("emp2"):
    print("exists")
else:
    print("not exist")
    
    
    