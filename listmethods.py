alist = [10,20,30]
alist.append(40)
print("After appending :", alist)
alist.append(34)
alist.append(45)
print("After appending :", alist)
alist.extend([56,34,12,54546])  # multiple values
print("After extending :", alist)
alist.insert(0,5) # insert( where to insert , what to insert)
alist.insert(2,900)
print("AFter inserting :", alist)

getcount =  alist.count(10)
print("10 is repeated for :", getcount)

alist.pop()   # remove value at last index by default
print("After pop :", alist)
alist.pop(0) # value at index 0 will be removed
print("After pop :", alist)
alist.pop(4)# 4 is the index no.
print("After pop :", alist)
alist.remove(20) # will remove 20 directly ( indexing is NOT used)
print("After remove :", alist)

alist.sort()
print("list elements after sorting:", alist)

alist.reverse()
print("list elements after reversing:", alist)









