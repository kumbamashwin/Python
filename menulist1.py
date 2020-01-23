# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:32:12 2020

@author: ashwin.kk
"""

import os
import sysconfig

def versioninfo():
    sysconfig.get_python_version()
    print(versioninfo)
    
print("=============Optiions===================")
print("1.display version if python")

choice = input("Enter your choice:")

if choice == 1:
    versioninfo()
    