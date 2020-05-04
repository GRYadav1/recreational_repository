'''
Created on 21-Feb-2020

@author: gaura
'''

def getString(dict):
    for key, value in dict.items():
        k1 = str(key)
        v1 = str(value)
    if(key and value):    
        return k1 + v1
    else:
        return k1


def CountAndSay(num):
    initial=1
    
    items = dict()
    items[initial] = 0   
    
    while():
        retval=getString(items)
        print(retval)
        for i in retval:
            if(i!=0):
                items[int(i)]=items[int(i)]+1 
        break
    print(items)
    return retval


if __name__ == '__main__':
    print(CountAndSay(4))