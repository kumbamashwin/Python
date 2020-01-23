#method1
with open("employees.txt","r") as fr:
    for line in fr:
        #remove 
        line=line.strip()
        print(line)


#method 2
#reading the file line by line using readlines
with open("employees.txt","r") as fr:
    print(fr.readlines()) 

#menhod 3 
#reading the file to the string
with open("employees.txt","r") as fr:   
    print(fr.read())
    
    
    #menthod 4
    #using csv libraries
import csv

with open("employees.txt","r") as fr:
#converting file object to csv object
    reader = csv.reader(fr)
    for line in reader:
        print(line)    