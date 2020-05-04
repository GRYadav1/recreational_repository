'''
Created on 14-Mar-2020

@author: gaura
'''

def sum2(a,target):
    returned = []
    
    front,rear = 0,len(a)-1
    a= sorted(a)
    while(front<rear):
        
        if(a[front]+a[rear]<target):
            front+=1
        else:
            if (a[front] + a[rear]>target):
                rear -=1
            
            else:
                returned.append(a[front])
                returned.append(a[rear])
                break
    return returned  

def sum3(nums,target):
    returned = []
#     for i in range(0,len(a)):
#         returned = a[:i] + a[i+1:]
#         ret=sum2(returned,-a[i])
#         ret.append(a[i])
#     return ret
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    results = []
    for i in range(len(nums)-2):
        if(i == 0 or (i>0 and nums[i]!=nums[i-1])):
            left = i+1
            right = len(nums)-1
            
            sum = 0 - nums[i]
            
            while(left<right):
                
                if(nums[left]+nums[right]==sum):
                    results.append([nums[i],nums[left],nums[right]])
#                     while(left<right and nums[left]==nums[left+1]):
#                         left+=1
#                     while(left<right and nums[right]==nums[right-1]):
#                         right -= 1
                    left+=1
                    right-=1
                
                elif nums[left]+nums[right]<sum:
                    left+=1
                    
                else:
                    right-=1
    return results
   
def main():
    print(sum3([-1, 0, 1, 2, -1, -4],1))
    
main()