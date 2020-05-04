'''
Created on 31-Jan-2019

@author: gaura
'''

def checker(ms, ts):

    listmark = [0]* len(ts)
    listTs=[]
    i=0
    for item in ts:
    
        listTs.append(item.split(' '))
        i=i+1
   
    flag1 = 0 
    i=0
    
    for text in ms:
        
        for p in listTs[i]:
            if(text.find(p)!=-1):
                 flag1=flag1+1
                    
            i=i+1               
            if (flag1==len(listTs[i])):
                 listmark[i]=1
         
            i=i+1   
         
        
    print(listmark)    
             
def main():
    s = ['I am using Eclipse','I love Pizza', 'I love sandwich']
    t = ['I love','Pizza']
    
    print(s)
    print(t)
    ret=checker(s,t)
    print(ret) 
    
main()    
       
        
        