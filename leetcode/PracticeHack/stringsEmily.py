
def hourGlass(arr):
    sum1 = 0
    count= 0
    for i in range(0,4):
        count = 0
        j= i
        sum1 = 0
        while(j<4):
            if(count==0):
                 sum1 = sum1 + arr[i+1][j+1]
            if(count<3):    
                 sum1= sum1+ arr[i][j]
                 sum1 = sum1 + arr[i+2][j]
                 count=count+1
            j=j+1
        print("Sum:",sum1)         
                    
                
        


def main():
    Arr=[[1, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 2, 4, 4, 0],
          [0, 0, 0, 2, 0, 0],
          [0, 0, 1, 2, 4, 0]]
    
               
    hourGlass(Arr)
    
main()    