'''
Created on Nov 21, 2018

@author: gaurav
'''


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

def initialize(node,edge):
    global graph
    #inf = int("inf")
    graph=[[ INT_MAX for i in range(0, node)] for j in range(0,node)]
    #global vertices
    #vertices=[0 for i in range(0, node)]


def MSTPrims(G,start):
    
    V = len(vertices)
    key = [INT_MAX]* V
    parent = [None]* V
    
    mstSet = [False]* V
    parent[start]= -99
    key[start]=0
    sum=0
    for i in range(0,V):
        
        u = minDistance(key, mstSet, V)
        
        mstSet[u] = True
        
        for j in range(0,V):
             
            if int(G[u][j]) > 0 and mstSet[j] == False and key[j] > int(G[u][j]):
                key[j]= int(G[u][j])
                parent[j]=u
        #print(key)         
    for i in range(0,V):
        sum+=key[i]
    print("==========")        
    printAnswer(parent, V, start)
    print("-------------")
    print("Total Cost:",sum)
        
    
def printAnswer(parent,V, start):
    
    print("Edge    Cost")
    print("---------------")
    for i in range(0,V):
        if parent[i]<0:
            continue
        print(vertices[parent[i]][1],"-", vertices[i][1],"     ", 0 if i==start else graph[i][parent[i]])
             
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
    
    
    print("Vertices:",nodes,"Edges:",edgnum,"start:",sn)
    print("-------")
    MSTPrims(graph, findnum(sn))
        
main()

