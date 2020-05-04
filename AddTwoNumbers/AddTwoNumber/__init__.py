class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def rev_num(stack1):
    num = 0
    while(stack1):
        num = num *10 + stack1.pop()
    
    return num

def addnumber(l1,l2):
    
    ptr1 = l1
    ptr2 = l2
    stack1 = []
    stack2 = []
    while(ptr1!=None):
        stack1.append(ptr1.val)
        ptr1 = ptr1.next

    while(ptr2!=None):
        stack2.append(ptr2.val)
        ptr2 = ptr2.next
        
    num1= rev_num(stack1)
    num2= rev_num(stack2)
    
    sum = num1+num2
    p = ListNode(0)
    final_list = p
    while(sum!=0):
        p.next = ListNode(sum%10)
        p = p.next
#         finalstack.append()
        sum = int(sum/10)
    
    p.next = None
    if(final_list.next):      
        final_list = final_list.next
    
#     while(final_list!=None):
#         print(final_list.val)
#         final_list = final_list.next
    return final_list
    

def main():
    l1 = ListNode(0);
    l2 = ListNode(4);
    l3 = ListNode(3);
    l4 = ListNode(0);
    l5 = ListNode(6);
    l6 = ListNode(4);
    
    
    l1.next = None
    l2.next = l3
    l3.next = None
    l4.next = None
    l5.next = l6
    l6.next = None
    
    print(addnumber(l1,l4))
    

main()
    

    
    
    