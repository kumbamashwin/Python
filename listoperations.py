
# empty tuple
atup = ()
# converting to list
alist = list(atup)
alist.append('unix')
alist.extend(['spark', 'scala','hadoop','sccm'])
alist.extend(['c','cpp','java','salesforce','sap','unix' ])

alist.remove('java')
alist.remove('salesforce')

alist.insert(0,'oracle')
alist.insert(5,'mongodb')

alist.reverse()

print(alist)

print("Total no. of elements are :", len(alist))

print("Unix count :", alist.count('unix'))