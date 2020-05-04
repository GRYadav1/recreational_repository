'''
Created on Sep 6, 2018

@author: gaurav
'''

from ex3 import studR;
              
  
print("Welcome to the birthday records, we know birthdays of ");

for keys in studR:
    print(keys);

name = input("Who's birthday you want to look up (Enter Name): ");   

print(name+"'s birth date is  "+studR[name]);

         