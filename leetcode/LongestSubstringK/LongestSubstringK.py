class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        kk = s.count
        c = min(set(s), key=kk)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))

def main():
    print(Solution().longestSubstring('aaabb', 3))
    
main()
