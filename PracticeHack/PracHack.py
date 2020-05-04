
from collections import Counter
from collections import defaultdict

def defaultvalue():
    return 0;

def countTriplets(prices,amount):
    
    prices=sorted(prices)
    n = len(prices)
    i=0
    count = 0
    k = amount
    while(i<n and prices[i]< k):
        if(prices[i]<=amount):
            count+=1
        amount=amount - prices[i]
        print(amount, count)
        i+=1
                         
     
    return count;

def main():
    
    text1 = [1, 12, 5, 111, 200, 1000, 10]
    text2 = [1,2,3,4]
    
    print("Hi")    
   # print(checkfact(3))    
            
    ret = countTriplets(text2,7)
    
    print(ret)
    
main()    