'''
Created on Nov 8, 2018

@author: gaura
'''
import math
import os
import random
import re
import sys

def climbingLeaderboard(scores, alice):
    rank=[0]*len(scores)
    temprank=0
    i=0
    r=1
    for x in range(0,len(scores)):
        rank[i]=r
        if scores[x]==scores[x-1]:
            rank[i]=rank[i-1]
            r=r-1
        i+=1
        r+=1    
        
    end_l = len(scores)-1
    start = scores[0]
    end = scores[end_l]
    middle = scores[int(end_l/2)]
    alicerank=[0]*len(alice)
    i=0
    for x in alice:
        if(x<=middle):
            s=int(end_l/2)
            end= end_l
            
        else:
            s=0
            end= int(end_l/2) 

        for y in range(s,end+1):
            if scores[y]>x:
                continue
            elif scores[y]==x:
                 alicerank[i]=rank[y]
                 break   
            elif scores[y]< x:#tscores.insert(y,x)
                 alicerank[i]=rank[y]
                 break
        if(alicerank[i]==0):
            alicerank[i]=rank[y]+1    
        i=i+1    
    print(alicerank)    
    #print(rank)
if __name__ == '__main__':
    scores=[100,90, 90, 80, 75, 60]
    alice =[50, 65, 77, 90, 102]

    result = climbingLeaderboard(scores, alice)

    print(result)
