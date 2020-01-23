## fron current dir
#
#import os
#try:
#    for file in os.listdir():
#        print(file)
#        
#except Exception as err:
#    print(err)
#
#
##from D dir
#    
#import os
#path = "C:\\"
#print("**********",path,"**********")
#try:
#    for file in os.listdir(path):
#        print(file)
#except Exception as err:
#    print(err)
    
    
    ## displaying .py files from current path
    
#import os
#try:
#    for file in os.listdir():
#        if file.endswith(".py"):
#            print(file)
#except Exception as err:
#        print(err)
    
    # display files and directories
#import os
#
#dirlist = []
#filelist=[]
#
#try:
#    for file in os.listdir():
#        if os.path.isfile(file):
#            filelist.append(file)
#        elif os.path.isdir(file):
#            dirlist.append(file)
#except Exception as err:
#    print(err)
#else:
#       
#       print("--------------FILES--------")
#       for file in filelist:
#           print(file)
#       print("--------------Dir--------")
#       for file in dirlist:
#           print(file)
#           
#           ## file size
# 
#import os
#
#try:
#    for file in os.listdir():
#        if os.path.isfile(file):
#            getsize = os.path.getsize(file)
#            print (file.ljust(40),getsize,"bytes")
#except Exception as err:
#        print(err)
    
    #delete all .pdf files
    
#            
#import os
#
#try:
#    for file in os.listdir():
#        if file.endswith(".pdf"):
#         os.remove(file)
#except Exception as err:
#       print(err)
    
    
                
#import os
#
#try:
#    for value in range(1,100):
#        dirname = "dir" + str(value)
#        os.rmdir(dirname)
#except Exception as err:
#       print(err)
    
    #copy files
    
#import shutil
#import os
#
#source = "C:\\Users\\ashwin.kk\\Desktop\\programs\\source"
#destination = "C:\\Users\\ashwin.kk\\Desktop\\programs\\destination"
#os.chdir(source)
#try:
#    if os.path.isdir(source) and os.path.isdir(destination):
#        for file in os.listdir():
#            if os.path.isfile(file):
#                shutil.copy(file,destination)
#                print(file, "copied to ", destination)
#    else:
#        print("directories are not existing")
#except Exception as err:
#       print(err)
#    
    
import os
import time
try:
    for file in os.listdir():
        today_date = time.strftime("%d-%m-%Y_")
        if file.endswith("csv"):
            newfile =today_date + file
            
            os.rename(file,newfile)
            print(file, "------------>" + newfile)
except Exception as err:
       print(err)            