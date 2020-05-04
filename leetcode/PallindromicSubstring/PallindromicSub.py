class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        
        for i in range(0,len(s)):
            print(i,s[i]+'\n------')
            len1 = self.expandMiddle(s, i, i)
            len2 = self.expandMiddle(s, i, i+1)
            len3 = max(len1,len2)
            print(len3)
            if(len3>(end-start)):
                start = i - int((len3-1)/2)
                end = i + int((len3)/2)
                
        ret=s[start:end+1]
        return ret
        
    def expandMiddle(self,s,left,right):
        if(s==None or s=='' or left>right):
            return 0
        
        while(left>=0 and right<len(s) and s[left]==s[right]):
            print(s[left],s[right])
            left-=1
            right+=1
            
        return right-left-1
        
        
def main():
    s = Solution()
    print(s.longestPalindrome("bbaabb"))

main()    