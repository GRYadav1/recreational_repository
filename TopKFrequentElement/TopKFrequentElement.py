'''
Created on 19-Apr-2020

@author: gaurav
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        
        for i in nums:
            dict[i]=0
        
        for i in nums:
            dict[i]+=1
            
        sorted_d = sorted(dict.items(), key=lambda x: x[1],reverse=True)
        return sorted_d[:k+1]

def main():
    print(Solution().topKFrequent([1,1,1,2,3], 2))
    
main()