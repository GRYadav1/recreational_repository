class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ''
        currentCharacter = 'a' if A >= B else 'b'
        
        while A > 0 or B > 0:
            if currentCharacter == 'a':
                res += 'aa' if A > B and A > 1 else 'a'
                A -= 2 if A > B and A > 1 else 1
                currentCharacter = 'b'
            else:
                res += 'bb' if B > A and B > 1 else 'b'
                B -= 2 if B > A and B > 1 else 1
                currentCharacter = 'a'
        
        return res
    
def main():
    print(Solution().strWithout3a3b(1,4))
    
main()