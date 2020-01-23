
import urllib.request
import csv
#url to download
link = "http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv"
filename = link.split("/")[-1]
#download the file to local directory
urllib.request.urlretrieve(link,filename)

paymentset = set()
with open(filename,"r") as obj:
    header=obj.readline()
    reader = csv.reader(obj)
    for line in reader:
        paymentset.add(line[3])
    for payment in paymentset:
        print(payment)
            
     