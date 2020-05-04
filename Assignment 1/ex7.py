'''
Created on Aug 30, 2018

@author: gaurav
'''
import os
from datetime import datetime


def getSizeofFile(filename):
    st = os.stat(filename)
    return st.st_size

def getDuration(seconds):
    return(datetime.fromtimestamp(seconds).strftime('%Y-%m-%d %H:%M:%S'));
      
    

# Enter Path to be read.
path = input("Enter the path to be read (eg E:/Abc/Folderpath):");
#path = 'E:/Chrome-Downloads/Software-Stuff'

# read the entries
with os.scandir(path) as listOfEntries:  
    print("Filename"+ '\t\t\t\t\t\t'+" Size  "+'\t\t\t' +" Last Modified")
    print("\n-----------------------------------------------------------------------------------------------")
    for entry in listOfEntries:
        # print file names
        if entry.is_file():
            
            print(entry.name, '\t\t\t\t', getSizeofFile(path+'/'+entry.name),"Bytes ", '\t\t',getDuration(os.path.getmtime(path+'/'+entry.name)));