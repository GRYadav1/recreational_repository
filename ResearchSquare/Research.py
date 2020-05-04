'''
Created on 09-Mar-2020

@author: gaura
'''

# Python function that checks if a number between 1-100 is a multiple of 3,5 or both and prints text accordingly.
def checkMultiple():
    
    for i in range(1,101):
#        if number is a multiple of 3 and 5
        if(i%3==0 and i%5==0):
            print(i,'Research_Square')
        else:
#           if number is divisible by 3  
            if(i%3==0):
                print(i,'Research')
#            if number is divisble by 5
            else:
                if(i%5 == 0):
                    print(i,'Square')
                    

checkMultiple() 