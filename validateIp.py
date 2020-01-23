ipaddr = input("enter the ip:")

iplist = ipaddr.split(".")

# map(funtction,list)
iplist = list(map(int,iplist))

if len(iplist) == 4:
    if iplist[0] in list(range(1,256)) and iplist[1] in list(range(1,256)) and iplist[2] in list(range(1,256)) and iplist[3] in list(range(1,256)):
        print ("valid IP")
    else :
        print("invalid Ip")