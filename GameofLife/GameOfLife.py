'''
Created on 21-Apr-2020

@author: gaura
'''

import copy

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        row = len(board)
        col = len(board[0])
        OrigBoard = copy.deepcopy(board)         
        for i in range(row):
            for j in range(col):
                
                countAlive = 0
                for n in neighbors:
                    
                    r = i+n[0]
                    c = j+n[1]
                    
                    if(r>=0 and r<row and c>=0 and c<col and OrigBoard[r][c]==1):
                        countAlive+=1
                        
                #Rule 1 and 3    
                if((countAlive<2 or countAlive>3) and OrigBoard[i][j]==1):
                    board[i][j] = 0
                    
                #Rule 4
                if(OrigBoard[i][j]==0 and countAlive==3):
                    board[i][j]=1
                        
                        
        return board           
        


def main():
    
    board = [ [0,1,0],
              [0,0,1],
              [1,1,1],
              [0,0,0]]
    print(Solution().gameOfLife(board))
    
main()
        