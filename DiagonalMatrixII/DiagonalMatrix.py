'''
Created on 02-May-2020

@author: gaurav
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
#         queue = []
#         visited = []
#         queue.append(s)
#         visited.append(s)
#         flag = False
#         while(len(queue)>0):
#             
#             currentWord = queue.pop(0)
# #             visited.append(currentWord)
#             
#             if(currentWord in wordDict):
#                 flag = True
#             
#             else:
#                 count =0
#                 for i in wordDict:
#                     
#                     if i in currentWord:
#                         preWord = currentWord[:currentWord.index(i)]
#                         postWord = currentWord[currentWord.index(i)+len(i):]
#                         if(len(preWord)!=0 and preWord not in visited):
#                             queue.append(preWord)
#                             visited.append(preWord)
#                         if(len(postWord)!=0 and postWord not in visited):
#                             queue.append(postWord)
#                             visited.append(postWord)
#                         count+=1
#             
#             if(count==0):
#                 return False
#         return True
        queue = [0]
        slen = len(s)
        lenList = [l for l in set(map(len,wordDict))]
        visited = [0 for _ in range(0, slen + 1)]
        while queue:
            tmpqueue = []
            for start in queue:
                for l in lenList:
                    if s[start:start+l] in wordDict:
                        if start + l == slen:
                            return True
                        if visited[start + l] == 0:
                            tmpqueue.append(start+l)
                            visited[start + l] = 1
            queue, tmpqueue = tmpqueue, []
        return False


def main():
    s = "abcd"
#     wordDict = ['leet','code']
#     wordDict = ["apple", "pen"]
#     wordDict = ["cats", "dog", "sand", "and", "cat"]
    wordDict = ["a","abc","b","cd"]
    print(Solution().wordBreak(s, wordDict))
    
main()