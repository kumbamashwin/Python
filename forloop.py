#for loop with range()
for val in range(1,11):
    print (val)

#for loop with list

alist = [10,20,30,40]
for val in alist:
    print(val)  
    
## for loop with string
    
string = 'python'
for char in string:
    print(char)
    
# for loop with tuple
    
atup =  ('unix','java','c++')
for item in atup:
    print(item)
    
#for loop with dictionary

book = {"chap1":10,"chap2":20,"chap3":30}
for key in book.keys():
    print(key)
    
book = {"chap1":10,"chap2":20,"chap3":30}
for key,value in book.items():
    print(key,value)
    
    ## for loop with set
    
aset = {10,10,10,20}
for val in aset:
    print(val)
    
## displaying all unique values from list

alist = [10,10,10,20,20,20,20,30,30,30]
uniquevalues = set(alist)
for val in uniquevalues:
    print(val)
    
### or####
    
alist = [10,10,10,20,20,20,20,30,30,30]
for val in set(alist):
    print(val)
    
    ## display values in reverse order
    
for val in range(10,0,-1):
    print(val)
    
    ## display even numbers

    
    
    