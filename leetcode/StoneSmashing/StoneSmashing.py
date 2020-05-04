class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while(len(stones)>1):
            stones=sorted(stones,reverse=True)
            if(stones[0]==stones[1]):
                stones.pop(0)
                stones.pop(0)
            else:
                stones.append(stones[0]-stones[1])
                stones.pop(0)
                stones.pop(0)
        
        if(len(stones)):
            return stones
        return 0
        
def main():
    print(Solution().lastStoneWeight([1,3]))
    
main()