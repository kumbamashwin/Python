aset = {10,10,10,10,20,30}
bset = {30,40,50,50,50,50,50,40}
print(aset)
print(bset)

print("*********** UNION OPERATION ************")
print("All unique values of A and B :",aset.union(bset)) 
# OR
print(aset | bset)

print("********** INTERSECTION **************")
print(aset & bset)
# OR
print("All common values of A and B :", aset.intersection(bset))

print("*******   DIFFERENCE ************")
print(aset - bset)
# OR
print(aset.difference(bset))