'''
Created on 01-May-2020

@author: gaurav
'''
# from copy import deepcopy
# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         original = nums
#         h = set()
#         retArr = []
#         if(len(nums)==1):
#             retArr.append(nums)
#             return retArr
#         elif(len(nums)==2):
#             retArr.append(nums)
#             nums = deepcopy(nums)
#             nums[0],nums[1]=nums[1],nums[0]
#             retArr.append(nums)
#             return retArr
#         
#         for i in range(len(original)):
#             currentCopy = deepcopy(original)
#             currentCopy[0],currentCopy[i] = currentCopy[i],currentCopy[0]
#             h.add(tuple(currentCopy))
# #             print(h)
#             flag = True
#             while(flag):
#                 for j in range(1,len(currentCopy)-1):
# #                     print(j)
#                     currentCopy[j],currentCopy[j+1] = currentCopy[j+1],currentCopy[j]
#                     if tuple(currentCopy) not in h:
#                         h.add(tuple(currentCopy))
#                     
#                     else:
#                         print('Duplicate Found')
#                         flag = False
#                         break
#             
#         for i in h:
#             retArr.append(list(i))
#         print(len(retArr))
#         return retArr 
        
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        answer =[]
        return self.helper(nums,answer,[])
    
    def helper(self, nums,answer,rem):
        
        if(len(nums)==0):
            answer.append(rem)
            return       
        for i in range(len(nums)):
#             rem.append(list(nums[i]))
            self.helper(nums[:i]+nums[i+1:],answer,rem+[nums[i]])
            
        return answer
                  
def main():
    nums = [1,2]
    print(Solution().permute(nums))
    
main()