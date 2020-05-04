'''
Created on Oct 3, 2018

@author: gaura
'''

from time import time
import random

#Function for the insertion sort .
def insertionSort(arr): 
    #traversing the entire array till the length of the array
    for i in range(1, len(arr)): 
        #Moving the elements that are greater than the key to one index lesser than their current position .
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        

arr = []
n = int(input("Enter input Size:"))
for x in range(0,n):
    arr.append(random.randint(0,n))      
 
ts= time()  
insertionSort(arr) 
te= time()
print(arr) 
print("Execution TIme :", te-ts) 
