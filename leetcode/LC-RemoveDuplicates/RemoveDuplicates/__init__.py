#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strangeSort' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY mapping
#  2. STRING_ARRAY nums
#

def strangeSort(mapping, nums):
    # Write your code here
    k={mapping[i]:i for i in range(len(mapping))}
    #print('dict',k)
    sum1 = 0
    l=[]
    for i in nums:
        for j in i:
            temp=k[int(j)];
            # print(temp,'',j)
            sum1 = sum1 * 10 + temp
        print(sum1)
        l.append(sum1)
        sum1=0
    n=len(l)
    print("Before sort",nums)
    print("Before list",l)
    quicksort(l,0,n-1,nums)




    
    #for i in range(len(l)-1,0,-1):
     #   for j in range(i):
      #      if int(l[j])>int(l[j+1]):
       #         t=l[j]
        #        l[j]=l[j+1]
         #       l[j+1]=t
          #      t=nums[j]
           #     nums[j]=nums[j+1]
            #    nums[j+1]=t
    print("After sort",nums)
    print("After list",l)
        
    return nums    

def quicksort(arr,low,high,nums):
    if low<high:
        pi=partition(arr,low,high,nums)

        quicksort(arr,low,pi-1,nums)
        quicksort(arr,pi+1,high,nums)

def partition(arr,low,high,nums):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
            nums[i],nums[j]=nums[j],nums[i]
    
    arr[i+1],arr[high]=arr[high],arr[i+1]
    nums[i+1],nums[high]=nums[high],nums[i+1]
    return i+1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mapping_count = int(input().strip())

    mapping = []

    for _ in range(mapping_count):
        mapping_item = int(input().strip())
        mapping.append(mapping_item)

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = input()
        nums.append(nums_item)

    result = strangeSort(mapping, nums)

    fptr.close()
    