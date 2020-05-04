'''
Created on 03-Feb-2020

@author: gaura
'''
def allContainPrefix(s,s_first, start,end):
    
    for i in range(0,len(s)):
        word = s[i]
        for j in range(start,end+1):
            if(word[j]!=s_first[j]):
                return False
        
    return True;

def longestPrefix(s):
    
    index = len(min(s, key = len))
    
    prefix = ""
    
    low,high=0,index-1
    
    while(low<=high):
        
        mid = int(low + (high-low)/2)
        
        if allContainPrefix(s,s[0], low,mid):
            
            prefix = prefix + s[0][low:mid + 1]
            
            low = mid +1
        else:
            high = mid - 1
            
    return prefix
             
    
    

def main():
    
    print(longestPrefix(["flower","flow","flight"]))
    
    
main()    