'''
Created on 20-Apr-2020

@author: gaura
'''
class Solution(object):
    def intersect(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        if(len(num1)>=len(num2)):
            bigger = num1
            smaller = num2
        else:
            bigger = num2
            smaller = num1
        
        dict = {}
        
        for i in bigger:
            dict[i]=0
            
        
        for i in bigger:
            dict[i]+=1
        
        
        for i in smaller:
            
            if(i in dict and dict[i]>0):
                ret.append(i)
                dict[i]-=1
            
        
        return ret

def main():
    print(Solution().intersect([4,9,5], [9,4,9,8,4]))
    
main()