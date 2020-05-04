'''
Created on Aug 26, 2018

@author: gaurav
'''
from ex3 import studR
emails=[];


def decorator_example(argFunc):
    def inside_dec(argName):
            print("Creating email....")
            argFunc(argName);
          
    return inside_dec;         
    
@decorator_example    #Declairing decorator function   
def create_emails(argName):
    first = str(argName[0]);
    second= str(argName[1]);
    emails.append(str(first[0]+first[1]+second[0]+second[1]+"@uncc.edu")); 
   

for rec in studR.keys():
        name= str(rec);
        fullname = name.split();
# Passing name of a student to decorator function
        create_emails(fullname);
 
#(emails);   
print(emails)   #Print the entire emails array.  
    

    
    
    
    
  
    
    