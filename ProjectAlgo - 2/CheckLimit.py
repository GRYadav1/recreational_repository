def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#         sorted_list = sorted(nums)
        sorted_list = nums
        l=0
        r=len(sorted_list)-1
        answer =[1]
        while(l<=r):

            if((sorted_list[l]+sorted_list[r]) > target):
                r-=1;

            if((sorted_list[l]+sorted_list[r])== target):
                x=l
                y=r
                break;
            
            if((sorted_list[l]+sorted_list[r]) < target):
                l+=1;

        if(x or y):
#             left = nums.index(x)
#             right= nums.index(y)
            left=x
            right=y
            return left,right
        
        else:
            return 0,0


def main ():
    print(twoSum([3,2,4], 6))


main()
