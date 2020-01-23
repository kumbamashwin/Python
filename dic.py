

infodoc =  { 2001: {"ap":70}  , 2002:{"tn":75} , 2003:{"up":50} }

print("state".ljust(10), "literacy rate")
print("----------------------")

for value in infodoc.values():
    #print(value)
    for key,value in value.items():
        print(key.ljust(10),value)
        
        
    