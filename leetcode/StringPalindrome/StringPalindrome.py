class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        allSubs = []
        
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                allSubs.append(s[i:j])
                
        return self.checkPalindromes(allSubs)
    
    def checkPalindromes(self,allSubs):
        
        count = 0
        for string in allSubs:
            i = 0
            j = len(string)-1
            while(i<=j):
                if(string[i]==string[j]):
                    i+=1
                    j-=1
                else:
                    break
            if(i>j):
                count+=1
        return count
            
                

def main():
    print(Solution().countSubstrings('ababab'))
    
main()