'''
Created on Oct 2, 2018

@author: gaurav
'''
import random
from time import time

def merge(arr, l, m, n):
    
    firstHalf = m-l+1
    secondHalf =n-m
    
    FirstH = [0] * firstHalf
    SecondH = [0] * secondHalf
    
    for i in range(0, firstHalf):
          FirstH[i] = arr[l+i]    
          
    
    for j in range(0, secondHalf):
          SecondH[j] = arr[m+j+1]
          
    i = 0;j = 0;k = l
    
    while(i< firstHalf and j < secondHalf):
           if (FirstH[i] <= SecondH[j]):
              arr[k] = FirstH[i]
              i = i + 1
           else:
              arr[k] = SecondH[j]
              j= j + 1
           k =k + 1 

    while(i<firstHalf):
        arr[k]= FirstH[i]  
        i=i+1
        k=+1
        
    while(j<secondHalf):
        arr[k]=SecondH[j]
        j=j+1
        k=k+1 
              
    
    
def mergeSort(arr,l,n):

     if l < n: 
         m = int((l+(n))/2)
         mergeSort(arr, l, m) 
         mergeSort(arr, m+1, n)
         merge(arr,l,m,n) 
     

arr = []
n = int(input("Enter input Size:"))
for x in range(0,n):
    arr.append(random.randint(0,n))        
   
ts = time();    
mergeSort(arr, 0, n-1)
print(arr)
te = time()
print("#### Time required",te-ts,"\n\n\n")
    
    
    
