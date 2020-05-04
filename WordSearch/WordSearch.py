class Solution(object):
   
    visited = [[
                ]
               ]
    def searchDFS(self,i,j,index,board,word):
        
        if(len(word)==index):
            return True
        
        if(i< 0 or i>=len(board) or j< 0 or j>=len(board[i]) or word[index]!=board[i][j]):
            return False
        
        temp = board[i][j]
        board[i][j] = ' '
        if( self.searchDFS(i+1,j,index+1,board,word) or
            self.searchDFS(i-1, j, index+1, board, word) or
            self.searchDFS(i,j+1, index+1, board, word) or 
            self.searchDFS(i,j-1, index+1, board, word)):
            return True
        
        board[i][j] = temp
        return False
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.searchDFS(i,j,0,board,word):
                    return True
    
        return False   


def main():
    board =[
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
            ]
            
    word = 'SEE'
    s = Solution()
    print(s.exist(board,word))

main()
    