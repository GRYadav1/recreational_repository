'''
Created on Aug 25, 2018

@author: gaurav Yadav

Use of Dictonary Data type for student record and printing the same record.
'''


from ex3 import studR; #Importing StudRecord from previous program;
            
  
def displayDict(Arg):   # Display Function Definition
    for keys in Arg:
        print(keys);
        print(Arg[keys]);
        print("------------------------")     

                       
            
                     
displayDict(studR);  # Calling Display Function