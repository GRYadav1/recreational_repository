class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd = 0
        even = 0
        for i in range(len(nums)):
            if(i%2==0):
                even +=nums[i]
                
            else: odd+=nums[i]
                
        
        return max(odd,even)
    
def main():
    print(Solution().rob([1,2,3,1]))
    
main()