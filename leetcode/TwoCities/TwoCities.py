class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        max_len=int(len(costs)/2)
        A = []
        B = []
        for i in costs:
            
            cur_min = min(i[0],i[1])
        
            ind = i.index(cur_min)
            
            if(ind ==0):
                if (len(A)!=max_len):
                    A.append(cur_min)
                    
            elif(len(B) != max_len):
                B.append(cur_min)        
        
        summ = 0
        for i in A:
            summ+=i
        for i in B:
            summ+=i
        return summ    
                    
        
         
def main():
     
    s= Solution()
    print(s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))

main()
