# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:48:55 2020

@author: ashwin.kk
"""
#function body
# fixed arguments
def display(first,second) :
    print(first,second)
#calling function
display (10,20)

#function body
#default arguments
def display(first=0,second=0,third=0) :
    print(first,second,third)
#calling function
display ()
display (10)
display (10,20)
display (10,20,30)

#function body
#variable lenght arguments
#if any object is prefixed with *, it is a tuple
def display(*data) :
    print(data)
    for val in data:
        print(val)
#calling function
display (1,2,3,4,4,54,55,43)


#function body
#variable lenght arguments
#if any object is prefixed with **, it is a tuple
def display(**book) :
    print(book)
    for key,value in book.items():
        print(key,value)
#calling function
display (chap1=10, chap2=20)




