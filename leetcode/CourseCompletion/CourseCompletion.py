'''
Created on 17-Apr-2020

@author: gaura
'''
from _collections import defaultdict

class Graph():
    def __init__(self,courses):
        self.graph = defaultdict(list)
        self.vertices = courses
        
    def addEdge(self,u,v):
        self.graph[u].append(v)


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = Graph(numCourses)
        
        for i in prerequisites:
            g.addEdge(i[0], i[1])
            
        visited = [False] * numCourses
        gstack = [False] * numCourses
        
        for i in range(numCourses):
            if(visited[i] == False):
                if(self.checkCycle(g, i, visited, gstack) == True):
                    return False
        
        return True
                
    
    def checkCycle(self,g,v,visited,gstack):
        
        visited[v] = True
        gstack[v] = True
        
        for neighbor in g.graph[v]:
            if(visited[neighbor] == False):
                if ( self.checkCycle(g, neighbor, visited, gstack) == True):
                    return True
            elif(gstack[neighbor] == True):
                return True
            
        
        gstack[v] = False
        return False
    
        
def main():
#     print(Solution().canFinish(2, [[1,0],[0,1]]))
      print(Solution().canFinish(5, [[0,1],[1,2],[4,3],[3,1],[2,3]]))
    
main()
        
        