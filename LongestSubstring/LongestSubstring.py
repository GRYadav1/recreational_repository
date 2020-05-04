'''
Created on 29-Feb-2020

@author: gaura
'''
import numpy as np
from itertools import permutations


def longestSubstring(inputstring):
    
    s = inputstring
    
#     res_str =[test_str[i: j] for i in range(len(test_str)) 
#           for j in range(i + 1, len(test_str) + 1)] 
#     lt = lambda pair: pair[0] < pair[1]
#     index_pairs = filter(lt, permutations(range(len(s)+1), 2))
#     res_str= list(s[i:j] for i,j in index_pairs)
    
#     print(res_str)
#     print(res_str)
    
    
#     for i in res_str:
#         dict={}
#         count=0
#         flag=1
#         max = 0
#         for j in i:
#             dict[str(j)]=count+1
#             if(dict[j]>1):
#                 flag = 1
#                 break
#             
#         if(max<len(i) and flag ==1):
#             max = len(i)
#     
#     print(max)
        
#     l1 = []
    input_str = inputstring
    max = 0
    for k in range((len(list(inputstring)),1)):
    
        unique_substrings = set(input_str[i: i + k] for i in range(len(input_str) - k + 1))
        sorted_substrings = sorted(unique_substrings)
    
        print(sorted_substrings)



#     max = 0    
#     for i in res_str:
#          
#         if(len(np.unique(list(i)))== len(list(i))):
#             if(max<len(list(i))):
#                 max = len(list(i))
                
    return max        
        
        

def main():
    
#     print(longestSubstring("lhdrxershqatgswgusoyupexdobckhzvqemnkfirwklcejkabyyypcvvqzxciyyacmpnsxeqjrsndfogdoevrcqjbnmjmmj"))
      print(longestSubstring("footballer"))
    
main()
    