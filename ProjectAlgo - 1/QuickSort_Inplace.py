import random
from time import time
#Function implementing the Inplace Quick Sort 
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

#Main Driver Code
arr =[]
n = int(input("Enter input Size:"))
for x in range(0,n):
     arr.append(random.randint(0,n))    

ts= time()
in_quicksort(arr,0,len(arr)-1)
te= time() 

print ("\n\nSorted array is") 
print (arr)

print("Time Required:",te-ts)