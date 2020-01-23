adict = {"chap1":10 ,"chap2":20}
print(adict) # displaying everything
print(adict.keys())  # display ONLY keys
print(adict.values())
#  [ (key1,value1) , (key2,value2)]
print(adict.items())
## accessing individual values
print(adict["chap1"]) #10
#print(adict["chap5"]) #
print(adict.get("chap5")) # None
print(adict.get("chap1"))
# adding key-value item
adict["chap3"] = 30
adict["chap4"] = 40
print("Afer adding :", adict)

adict.pop("chap1")   # will remove chap1:10 from dict
print("After removing :", adict)

adict.popitem(    # wull remove random key:value from dict
print("After popitem :", adict)