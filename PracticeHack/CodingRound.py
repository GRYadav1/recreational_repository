# Python3 program to print longest  
# palindromic subsequence 
  
# Returns LCS X and Y  
def lcs_(X, Y) : 
      
    m = len(X) 
    n = len(Y)  
  
    L = [[0] * (n + 1)] * (m + 1) 
  
    # Following steps build L[m+1][n+1]  
    # in bottom up fashion. Note that  
    # L[i][j] contains length of LCS of  
    # X[0..i-1] and Y[0..j-1] 
    for i in range(n + 1) : 
      
        for j in range(n + 1) : 
      
            if (i == 0 or j == 0) : 
                L[i][j] = 0;  
            elif ((X[i - 1]).lower() == (Y[j - 1]).lower()) : 
                L[i][j] = L[i - 1][j - 1] + 1;  
            else : 
                L[i][j] = max(L[i - 1][j], 
                              L[i][j - 1]);  
      
    # Following code is used to print LCS  
    index = L[m][n];  
  
    # Create a string length index+1 and  
    # fill it with \0  
    lcs = ["\n "] * (index + 1) 
  
    # Start from the right-most-bottom-most  
    # corner and one by one store characters  
    # in lcs[] 
    i, j= m, n  
    print(X,Y)  
    while (i > 0 and j > 0) : 
      
        # If current character in X[] and Y  
        # are same, then current character  
        # is part of LCS 
        print("x=",X[i-1], "y=",Y[j-1], end=" ")
        print("\n")
        if ((X[i - 1]).lower() == (Y[j - 1]).lower()) : 
            
            # Put current character in result  
            lcs[index - 1] = X[i - 1] 
            i -= 1
            j -= 1
  
            # reduce values of i, j and index  
            index -= 1
          
        # If not same, then find the larger of  
        # two and go in the direction of larger  
        # value  
        elif(L[i - 1][j] > L[i][j - 1]) : 
            i -= 1
              
        else : 
            j -= 1
      
    ans = "" 
      
    for x in range(len(lcs)) : 
        ans += lcs[x] 
      
    return ans 
  
# Returns longest palindromic  
# subsequence of str  
def longestPalSubseq(string) : 
      
    # Find reverse of str  
    rev = string[: : -1] 
      
    # Return LCS of str and its reverse  
    return lcs_(string, rev) 
  
# Driver Code 
if __name__ == "__main__" : 
  
    string = "RotornotSagas";  
    print(longestPalSubseq(string)) 
  
# This code is contributed by Ryuga