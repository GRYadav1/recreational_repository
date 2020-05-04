'''
Created on 01-May-2020

@author: gaurav
'''
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        h = {}
            
        for i in range(1,27):
            if(i<10):
                h[str(i)]=chr(96+i)
            else:
                h[str(i)+'#'] =chr(96+i)
        
        j = len(s)-1
        retString = ''
        buffer = ''
        
        while(j>=0):
            if(s[j]=='#'):
                buffer = s[j-2:j+1]
                retString+=h[buffer]
                j = j-2
                buffer = ''
            
            else: 
                retString+=h[s[j]]
            j=j-1
        
        return retString[::-1]
        
      
def main():
    s = '1326#'
    print(Solution().freqAlphabets(s))
    
main()