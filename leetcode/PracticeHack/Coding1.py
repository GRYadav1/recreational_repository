'''
Created on 19-Feb-2019

@author: gaura
'''
# A O(n^2) time and O(1) space program to find the  
#longest palindromic substring 
  
# This function prints the longest palindrome substring (LPS) 
# of str[]. It also returns the length of the longest palindrome 
def longestPalSubstr(string): 
    maxLength = 1
  
    start = 0
    length = len(string) 
  
    low = 0
    high = 0
  
    # One by one consider every character as center point of  
    # even and length palindromes 
    for i in range(1, length): 
        # Find the longest even length palindrome with center 
    # points as i-1 and i. 
        low = i - 1
        high = i 
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
  
        # Find the longest odd length palindrome with center  
        # point as i 
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
  
    print ("Longest palindrome substring is:",string[start:start + maxLength] )
  
    return maxLength 


def main():
       string = "RotornotSagas";  
       print(longestPalSubstr(string)) 
       
main()       
       
  