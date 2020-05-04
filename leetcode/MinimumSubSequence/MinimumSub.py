class Solution(object):
    
    def compareArray(self,target,arr):
        addition = 0
        for i in arr:
            addition+=i

        if(addition>=target):           
            return False
        return True 
    
    
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums,reverse=True)
        summation = 0
        dict = {}
        
        for i in range(len(nums)):
            summation +=nums[i]
            
            if(self.compareArray(summation, nums[i+1:])):
                dict[len(nums[:i+1])]= nums[:i+1]
                break
        
        
        
        for key,values in dict.items():
            return values
        
            
        
        
        
        
        
def main():
    
    print(Solution().minSubsequence([4,4,7,6,7]))
main()