'''
Created on 15-Mar-2020

@author: gaura
'''
 
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
class TreeNode(object):
    
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
        
    def printTree(self):
#         print(self.val)

        print(self.val)
        if(self.left):
            self.left.printTree()
        
        if(self.right):
            self.right.printTree()
            
            
    def insert(self,data):
        if(self.val):
            if(data<self.val):
                if(self.left is None):
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            
            elif(data>self.val):
                if(self.right is None):
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
    
class Solution(object):
    
    def findMiddle(self,root):
        
        count = 0
        while(root!=None):
            count+=1
            root = root.next
        return count
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.buildTree(head,0,self.findMiddle(head)-1)

    def buildTree(self,head,start,end):
        
        if(start>end):
            return None
        
        temp = head
        mid = int(start+(end - start)/2)
        
        d_start = 0
        while(d_start<mid and temp.next!=None):
            temp = temp.next
            d_start+=1
        
        root = TreeNode(temp.val)

        root.left = self.buildTree(head,start, mid-1)
        root.right = self.buildTree(head,mid+1, end)
        return root
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        h = set()
        return self.findSum(root,h,k,0)
    
    def findSum(self,root,h,k,found):
        
        if(root):
            if not k-root.val in h:
                h.add(root.val)
                self.findSum(root.left,h,k,found)
                self.findSum(root.right,h,k,found)
            else:
                found =1 
                
        if(found==1):
            return True
        else:
            return False      

def main():
    root1 = TreeNode(5)
    left1 = TreeNode(3)
    right1 = TreeNode(6)
    left1.left = TreeNode(2)
    left1.right = TreeNode(4)
    right1.left = None
    right1.right = TreeNode(7)

    root1.left = left1
    root1.right = right1
    
    
#     l1 = ListNode(-10)
#     l2 = ListNode(-3)
#     l3 = ListNode(0)
#     l4 = ListNode(5)
#     l5 = ListNode(9)
#     l1.next = l2
#     l2.next = l3
#     l3.next = l4
#     l4.next = l5
#     l5.next = None
#     
    s = Solution()
    root1.printTree()
    print(s.findTarget(root1, 9))
#     ret = s.sortedListToBST(l1)
#     ret.printTree()

main()