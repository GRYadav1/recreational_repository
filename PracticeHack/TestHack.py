'''
Created on 25-Mar-2019

@author: gaura
'''
'''
Created on 25-Mar-2019

@author: gaura
'''
import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    di = defaultdict(int)   
           
    for i in magazine:
        di[i] += 1
    count =0
    for text in note:
        if di[text]==0:    
            return "No";
        di[text]-=1
        
    return "Yes"               

if __name__ == '__main__':
    magazine = ["two", "times", "three", "is", "not", "four"]
    note = ["two", "times", "two", "is", "four"]
    
    print(checkMagazine(magazine, note))
