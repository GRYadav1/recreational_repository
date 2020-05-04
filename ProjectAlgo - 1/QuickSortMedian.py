'''
Created on Oct 6, 2018

@author: gaurav
'''
import random
from time import time
from turtle import done
import sys
sys.setrecursionlimit(100000)
    
def median_pivot(arr,l,r):
    median= int((l+r)/2)
    
    if(arr[median]<= arr[l]):
           temp = arr[median]
           arr[median] = arr[l]
           arr[l] = temp
           
    if(arr[median]> arr[r]):
           temp = arr[median]
           arr[median] = arr[r]
           arr[r] = temp
           
    if(arr[r]<arr[l]):
           temp = arr[r]
           arr[r] = arr[l]
           arr[l] = temp
    
    arr[median],arr[r-1]=arr[r-1],arr[median] 
    return arr[r-1]     
           
def insertionSort(sort_list, min, max):
    for i in range(min, max + 1):
        key = sort_list[i]
        j = i - 1
        while j >= min and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    return sort_list        

def quicksortmedian3(arr, left, right):
    
    if(left+10 <= right):
        
        pivot = median_pivot(arr, left, right)
        pivot_index = right-1 
        i=left
        j=right-2
    
        while done:
        
            while(arr[i] <= pivot and i<=j):
                i+=1 
        
            while(arr[j] > pivot and i<=j):
                j-=1
             
            if(i<j):
                arr[i],arr[j]=arr[j],arr[i]
            else:
                break
             
        arr[i], arr[right-1] = arr[right-1], arr[i]
        #pivot_index = i   
        quicksortmedian3(arr,left,i-1)
        quicksortmedian3(arr,i+1,right)
        
    else:
        #print("Performing INsertion Sort for <10")
        insertionSort(arr,left,right);
         
          
 
arr = []
n = int(input("Enter input Size:"))

for x in range(0,n):
    arr.append(random.randint(0,n))      

ts= time()  
quicksortmedian3(arr, 0, len(arr)-1) 

te= time()
print(arr) 
print("Execution Time :", te-ts)             