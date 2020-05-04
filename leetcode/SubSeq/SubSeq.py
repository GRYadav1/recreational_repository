

def functionfind(a):
    
    unique = []
    mark = [0] * 10
    print(mark)
    for i in range(len(a)):
        if a[i] not in unique:
            unique.append(a[i])
     
     
    for i in range(len(a)):
        mark[a[i]]= mark[a[i]] +1
         
    print(mark)
    returned = []
    for j in range(len(mark)):
        if(mark[j]>1 ):
            for k in range(1,mark[j]):
                if(mark[j]>1):
                    mark[j]-=1
                    returned.append(j)
    print(mark)
    print(returned)  

def main():
    
    functionfind([1,2,3,3,2,4])
main()