'''
Created on 20-Apr-2020

@author: gaura
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums = sorted(nums)
        
        half = (len(nums)//2)
        
        firstH = nums[:half]
        secondH = nums[half:]
        
        retArr = []
        f =0
        s =0
        i = 0
        while(i<len(nums)):
            if(i%2==0):
                retArr.append(firstH[f])
                f+=1
            else:
                retArr.append(secondH[s])
                s+=1
            i+=1
        return retArr
            

    
def main():
    print(Solution().wiggleSort([1, 3, 2, 2, 3, 1]))
    
main()