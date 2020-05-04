'''
Created on 24-Apr-2020

@author: gaura
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
#         for i in range(len(nums)):
#             if(nums[i]==0):
#                 temp = nums[i]
#                 nums = nums[:i]+nums[i+1:]
#                 nums.append(temp)
#                 

        index = 0
        
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[index]=nums[i]
                index+=1
            
        print(nums)       

        for i in range(index,len(nums)):
            nums[i] = 0
            
        return nums

def main():
    
    print(Solution().moveZeroes([0,0,0,0,0,1,0,3,12,0]))
    
    
main()