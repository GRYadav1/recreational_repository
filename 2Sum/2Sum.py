class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0 
        j = len(numbers)-1
        
        while(i<j):
            
            if(numbers[i]+numbers[j]<target):
                i+=1
            
            if(numbers[i]+numbers[j]>target):
                j-=1
                
            if(numbers[i]+numbers[j]==target):
                return [i,j]
            
        return None
 
def main():
     
    s = Solution()
    print(s.twoSum([2,7,11,15],9))

main()
