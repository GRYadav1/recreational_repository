'''
Created on 26-Apr-2020

@author: gaura
'''

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d = dict()
        
        for i in A:
            for j in B:
                s = i+j
                if( s not in d):
                    d[s]=0
                d[s]+=1
                
        print(d)
                            
        count = 0
        for k in C:
            for l in D:
                s = k+l
                print(s,count)
                if(-s in d):
                    count+=d[-s]
                
        return count
    
def main():
    A = [-1,-1]
    B = [-1,1]
    C = [-1,1]
    D = [1,-1]
    print(Solution().fourSumCount(A, B, C, D))
    
main()