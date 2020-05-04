'''
Created on 02-Apr-2020

@author: gaura
'''

class word:
    def __init__(self,word='',dist=0):
        self.word = word
        self.dist = dist
        

def ladderLength(beginword,endword,wordList):
    
    queue = []
    queue.append(word(beginword,1))
    visited =[]
    while(len(queue)):
        
        t = queue[0]
        queue.pop(0)
        
        if(t.word == endword):
            return t.dist
        
        currentWord = t.word
        
        for i in range(len(currentWord)):
            tempW = currentWord
            
            for j in range(ord('a'),ord('z')+1):
                tempW= tempW[:i] + chr(j) + tempW[i+1:]
                if tempW in wordList and not tempW in visited:
                    queue.append(word(tempW,t.dist+1))
                    visited.append(tempW)
    return 0
def main():
    
    print(ladderLength('leet', 'code', ["lest","leet","lose","code","lode","robe","lost"]))
    
main()
