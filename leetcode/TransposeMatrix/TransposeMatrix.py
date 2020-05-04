'''
Created on 03-May-2020

@author: gaura
'''
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])        
        answer = [[A[j][i] for j in range(row)] for i in range(col)]
        return answer
        

def main():
    A = [[1,2,3],[4,5,6],[7,8,9]]
    
    print(Solution().transpose(A))

main()