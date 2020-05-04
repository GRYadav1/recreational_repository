class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(nums)==1):
            return True
        i = 0
        maxJump = 0
        jump = nums[i]
        for i,jump in enumerate(nums):
            
            if(i>maxJump):
                return False
            
            maxJump = max(i+jump,maxJump)
#             i = maxJump
#             jump = nums[i]
        
        return True
            
    
            
    def calMaxJump(self,arr,index):
        maxx = -1
        maxIndex = 0
        
        for i in range(len(arr)):
            if(i+arr[i]>=maxx):
                maxIndex = i
                maxx = i+arr[i]
        
        return (index+maxIndex)
    
        
def main():
    
#     print(Solution().canJump([1,2,0,1]))
    print(Solution().canJump([2,3,1,1,4]))
#     print(Solution().canJump([3,2,1,0,4]))
#     print(Solution().canJump([1,1,2,2,0,1,1]))
      
        
main()