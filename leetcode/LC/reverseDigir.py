
class Solution(object):
    def rometoint(self, s):
        
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        prev_num = 0
        for i in s:
            if(dict[i] > prev_num):
                temp = (dict[i] - prev_num)
                sum = (sum-prev_num) + temp
                                
            else:
                sum = sum + dict[i]
            
            prev_num= dict[i]
            
            
        return sum; 
        return 0;
        


def main():
    C = Solution()
    print(C.rometoint('IV'))

main()    