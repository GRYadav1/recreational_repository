'''
Created on 29-Jan-2019

@author: gaura
'''
# Complete the countingValleys function below.
def thunderClouds(n, s):
    count=0
    i=0
    while(i<n-1):
        print("i=",i,"count=",count)
        if( i<n-2 and s[i+2]==0):
            count=count+1;
            i=i+1
        else:
            count=count+1    
        i=i+1     
    return count;

def main():
    ar =[0,0,1,0,0,1,0]
    n = 7
    ret = thunderClouds(n,ar) 
    print(ret) 
    
main()    