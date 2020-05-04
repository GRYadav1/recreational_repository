# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return l1


def mergelists(l1,l2):
    
    l1_index= 0
    l2_index= 0
    output_list= []
    for k in range(0, len(l1)):
        i = l1[k]
        if(l1[k]<=l2[k]):
            l1_index= l1_index+1
            output_list.append(l1[k])
        else:
            l2_index=l2_index+1    
                      
    
    
    return 0;



def main():
    
    list1= [1,2,4]
    list2= [1,3,4]
    
    print(mergelists(list1,list2))
main()    