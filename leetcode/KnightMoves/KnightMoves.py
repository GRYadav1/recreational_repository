'''
Created on 02-Apr-2020

@author: gaura

'''
class cell:
    def __init__(self,x=0,y=0,dist=0,parent=None):
        self.x = x 
        self.y = y 
        self.dist = dist
        self.parent = parent 

def isInside(x,y,N):
    if(x >=1 and x<=N and y >=1 and y<=N):
        return True
    return False

def knightMoves(startX,startY,endX,endY,N):
    
    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]
    
    visited = [[False for i in range(N+1)]
                      for j in range(N+1)]
    
    visited[startX][startY] =True
    
    queue = []
    queue.append(cell(startX,startY,0,None))
    
    while(len(queue)):
        t=queue[0]
        queue.pop(0)

        
        if(t.x == endX and t.y ==endY):
            return t
        

        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]
            
            if(isInside(x,y,N) and visited[x][y]==False):
                queue.append(cell(x,y,t.dist+1,t))
                visited[x][y]=True

def printPath(c):
    if(c!=None):
        print(c.x,c.y)
        printPath(c.parent)
    
                    
def main():
    
    startX = 1
    startY = 7
    endX = 1
    endY = 1
    N = 30
    printPath(knightMoves(startX,startY,endX,endY,N))
    
main()