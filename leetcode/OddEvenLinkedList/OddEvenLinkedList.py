class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        root = head
        i = 0
        while(head!=None):
            i+=1
            head=head.next
            
        head = root
        rootOdd = root        
        rootEven = root.next
        while(head.next.next!=None):
            temp = head.next
            head.next = head.next.next
            head = temp
            
        lastButOne = head
        lastOne = head.next
        lastButOne.next = None
        lastOne.next = None
        
        if(i%2!=0):
            lastOne.next = rootEven
        else:
            lastButOne.next=rootEven
        
        return root
        
        
        
        
        

def printSolution(root):
        while(root!=None):
            print(root.val)
            root = root.next
            
def main():
    
    listArr = [1,2,3,4,5]
    
    head = ListNode(listArr[0])
    root = head
    for i in range(1,len(listArr)):
        head.next = ListNode(listArr[i])
        head = head.next
    
    head.next = None
    printSolution(root)
    print("--------------")
    printSolution(Solution().oddEvenList(root))
main()