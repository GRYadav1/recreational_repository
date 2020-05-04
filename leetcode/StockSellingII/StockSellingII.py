from future.backports.xmlrpc.client import MAXINT
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
#          
#         for i in range(1,len(prices)):
#             if(prices[i]-prices[i-1]>0):
#                 profit += (prices[i]-prices[i-1])
#                  
#         return profit
#      
        
        minPrice = MAXINT
        maxPrice= 0
        for i in range(len(prices)):
            if(prices[i]<minPrice):
                minPrice = prices[i]
                
            elif (prices[i]-minPrice > maxPrice):
                    maxPrice  = prices[i]-minPrice
        
        return maxPrice
        
    
    
def main():
    print(Solution().maxProfit([7,5,4,3,2,9]))
    
main()