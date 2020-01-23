

import urllib.request
import csv
#url to download
link = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
filename = link.split("/")[-1]
#download the file to local directory
urllib.request.urlretrieve(link,filename)


#with open(filename,"r") as obj:
#    reader = csv.reader(obj)
#    for line in reader:
#        print("street name",line[0])
#        print("price",line[9])
#        print("-------------------")
        
#count = 0        
#with open(filename,"r") as obj:
#    reader = csv.reader(obj)
#    for line in reader:        
#        if line[-5] == "Residential":
#            count  = count + 1
#    print("total resi flats", count)


#cityset = set()
#with open(filename,"r") as obj:
#    reader = csv.reader(obj)
#    for line in reader:
#        cityset.add(line[1])
#    for city in cityset:
#        print(city)

citylist = []
with open(filename,"r") as obj:
    reader = csv.reader(obj)
    for line in reader:
        citylist.append(line[1])
        #displaying the output
        for city in set(citylist):
            print(city.ljust(15),"   ", citylist.count(city))
            
        

        
        