'''
Created on Nov 12, 2018

@author: gaurav
'''

import math
import heapq
import sys
from test.test_os import INT_MAX
vertices =[]
graph = [[]]

def minDistance(dist,splset,V):
    min_dist = float("inf")
    min_index=-99
    for i in range(0,V):
        if splset[i]== False and dist[i]<= min_dist:
            min_dist = dist[i]
            min_index= i

    return min_index

def assignNum(my_list):
    vrtxlist = sorted(set(my_list))
    global vertices
    vertices = list(enumerate(vrtxlist,0))
    #print(enumerate(vrtxlist,0))
    #print(vertices)

def addedge(row,col,num):
    global graph
    graph[row][col]=num
    

def findnum(a):
    ret1=0
    ret2=0
    for x in vertices:
        if x[1]==a:
            ret1 = x[0]
     
    return ret1             



def dijkstra(nodes,edges,sn):
    inf = float("inf")
    dist = [inf]* nodes
    cloud = [False]* nodes
    parent = [-1]*nodes
    dist[sn]=0 
    #heapq.heapify(dist)
    parent[sn]=sn
    for i in range(0,nodes-1):
        
        u = minDistance(dist, cloud, nodes)    
        cloud[u]= True
        #print("=====")
        for j in range(0,nodes):
            
            if(not cloud[j] and graph[u][j] and dist[u]!= inf 
               and (dist[u]+int(graph[u][j]))< dist[j]):
             
             dist[j]=dist[u]+ int(graph[u][j])
             parent[j]=u
        #print("Shortest Path to",vertices[i][1],":")     
        #printPath(parent,nodes,sn,i)   
        #print("----")              
    printAnswer(dist, nodes, sn,parent)
    
def printAnswer(distance,V,start,parent):
    print("EdgePath\tCost\tparent")
    print("------------------")
    for i in range(0,V):
        print(vertices[start][1],"-",vertices[i][1],"\t\t",distance[i],"\t", 'NA' if i == start else vertices[parent[i]][1])
    print("=========")
    for i in range(0,V):
    
        print("Shortest Path to ",vertices[i][1])
        printPath(parent, V, start,i)        
def printPath(parent,V,start,end):
    
    
    print(vertices[end][1],)
    i = end
    while(1):
        if (i == start):
            break
        print(vertices[parent[i]][1])
        i = parent[i]
        
    #print(vertices[i][1])    
def initialize(node,edge):
    global graph
    #inf = int("inf")
    graph=[[ INT_MAX for i in range(0, node)] for j in range(0,node)]
    #global vertices
    #vertices=[0 for i in range(0, node)]
    
def main():
    
    file1 = open("input.txt","r+")

    edges=[]
    vertx=[]
    global vertices
    i=0 
    sn = 'A'
    nodes =0 
    edgnum = 0
    while(1):
        text=file1.readline()
        text=text.rstrip()
        if(text=='' or text=='\n'):
            break
        
        if(i==0):
            nodes,edgnum,type=text.split()  
            i=+1
            continue
        s,e,w = text.split()
        vertx.append(s)
        vertx.append(e)
        edges.append([s,e,w])
    
    startNode = findnum(sn)
    nodes,edgnum=int(nodes),int(edgnum)
    assignNum(vertx)
    initialize(nodes,edgnum)
    for x in edges:
        row = findnum(x[0])
        col = findnum(x[1])
        addedge(row, col, x[2])
        if type =='U':
            addedge(col, row, x[2])
    
    
    print("Vertices:",nodes,"Edges:",edgnum)
    ''' Commenting this part since there have been some doubts over running 
        dijsktra for every node in graph'''
    ''' for i in range(0,nodes):
             dijkstra(nodes, edgnum, i) '''
    dijkstra(nodes, edgnum, findnum(sn)) 
        
main() 

    