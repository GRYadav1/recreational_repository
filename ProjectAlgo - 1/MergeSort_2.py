import random
from time import time

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
        

        
arr =[]        
 
n = int(input("Enter input Size:"))
for x in range(0,n):
     arr.append(random.randint(0,n))      
 
ts= time()  
mergeSort(arr,0,n-1)
te= time() 
print ("\n\nSorted array is") 
 
print (arr), 

print("time required : ",te-ts)
  

