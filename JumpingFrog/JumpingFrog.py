'''
Created on 08-Mar-2020

@author: gaura
'''
def jumpingFrog(a):
    
    start = a[0]
    end = a[len(a)-1]
     
    i = 0
    current = 0
    end = len(a)
    jumps = 0
    while(i<end):
        current = i + a[i]
         
        print(a[i])
        jumps+=1
        if(current>=end):
            break
        max = a[i]
        max_index = 0
        for j in range(i, current+1):
            if(max < a[j]):
                max,max_index = a[j],j
             
        if (max_index < j):
            current = max_index
        else:
            current = j     
        i = current
     
            
         
    return jumps

#     def jump(self, nums: List[int]) -> int:
#         preMax, curMax = 0, 0
#         jumps = 0
#         for i in range(len(a)-1):
#             curMax = max(curMax, a[i]+i)
#             if i == preMax:
#                 jumps+=1
#                 preMax = curMax
#         return jumps

if __name__ == '__main__':
    pass
#     array = [2,3,1,1,4]
#     array = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    array = [2,3,1,1,2,4,2,0,1,1]
    print(jumpingFrog(array))
    