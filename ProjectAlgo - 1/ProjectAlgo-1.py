'''
Created on Oct 7, 2018

@author: gaurav Yadav, Deekansha Tandon

'''

import random
from time import time
import copy
from turtle import done
import sys
sys.setrecursionlimit(100000)

# Function calculates pivot and swaps median with r-2 element
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

# Insertion Sort method            
def insertionSort(sort_list, min, max):
    for i in range(min, max + 1):
        key = sort_list[i]
        j = i - 1
        while j >= min and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    return sort_list        

#Quicksort routine based on median 3 method
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

#  In Place quicksort routine takes array and left,right indexes
def in_quicksort(s,x, y):
    def swapElements(s,x, y):
        temp = s[x]
        s[x] = s[y]
        s[y] = temp
    if x >= y: return
    pivot = s[y] 
    #pivot = random.randint(x,y)
    left = x
    right = y - 1
    while left <= right:
        while left <= right and s[left] <= pivot: 
            left += 1   
        while left <= right and s[right] >= pivot: 
            right -= 1  
        if left < right: 
            swapElements(s, left, right)
    swapElements(s, left, y)
    in_quicksort(s, x, left-1) 
    in_quicksort(s, left+1, y)


# MergeSort routine takes array l,mind,n indexes
def merge(arr, l, m, n): 
    first = m - l + 1
    second = n- m 
  
    firstarray = [0] * first
    secondarray = [0] * second
  
    for i in range(0 , first): 
        firstarray[i] = arr[l +i] 
  
    for j in range(0 , second): 
        secondarray[j] = arr[m +1+j] 
  
    i = 0;j = 0;p=l
    
    while i < first and j < second: 
        if firstarray[i] <= secondarray[j]: 
            arr[p] = firstarray[i] 
            i=i+ 1
        else: 
            arr[p] = secondarray[j]
            j += 1
        p=p+ 1
  
    while i < first: 
        arr[p] = firstarray[i] 
        i =i+ 1
        p =p+ 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < second: 
        arr[p] = secondarray[j] 
        j =j+ 1
        p += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be     sorted 
def mergeSort(arr,l,n): 
    if l <n: 
        
        m = int((l+(n-1))/2)
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, n) 
        merge(arr, l, m, n) 


# Input array and random number generation
arr = []
n = int(input("Enter input Size:"))
'''for x in range(0,n):
     arr.append(random.randint(0,n))
'''

'''for x in range(0,n):
        arr.append(x)
'''

k = n
for x in range(0,n):
    arr.append(k)
    k-=1
    
print(arr)
    
tQuickIn=0
for x in range(0,3):
    input3=copy.deepcopy(arr)
    ts=time()
    in_quicksort(input3,0,len(arr)-1)
    te=time()
    tf=te-ts
    tQuickIn+=tf
print("In-Place QuickSort :",tQuickIn/3)

tQuickMedian=0
for xtf in range(0,3):
    input4=copy.deepcopy(arr)
    ts=time()
    quicksortmedian3(input4, 0, len(input4)-1)
    te=time()
    tf=te-ts
    tQuickMedian+=tf
print("Median-3 Quick sort :",tQuickMedian/3)

tMerge=0
for x in range(0,3):
    input2=copy.deepcopy(arr)
    ts=time()
    mergeSort(input2,0,n-1)
    te=time()
    tf = te-ts
    tMerge+=tf
print("Merge Sort :", tMerge/3)

 

Tinsert=0     
for x in range(0,3):         
    input1=copy.deepcopy(arr) 
    ts= time()  
    insertionSort(input1,0,len(input1)-1) 
    te= time()
    tf = te-ts
    Tinsert+=tf
print("Insertion Sort :", Tinsert/3)



print("\n",input4) 
