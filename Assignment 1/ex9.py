'''
Created on Sep 3, 2018

@author: gaurav
'''

#Function definition for replace_string function
def replace_string(word):
   
    input_string=word.replace(word[0],"$");

    print(input_string);
    return 0    

#taske the input
word = input("Enter theString :");

#call replace_string function
replace_string(word);
