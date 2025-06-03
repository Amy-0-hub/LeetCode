# Definition for singly-linked list.
#A single linked list is a list made up of nodes that consists of two parts.
## 1.data: contains the actual data
## 2.link: contains the address of the next node of the list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional      

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:       
        head1 = list1
        head2 = list2
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        
        pointer1 = head1
        pointer2 = head2
        result = None   

        if head1.val <= head2.val:
            result = head1 
        else:
            result = head2
            
        previous_node = None
        while (pointer1 is not None) and (pointer2 is not None):
            if pointer1.val == 4 and pointer2.val == 4:
                print("here")
            if pointer1.val <= pointer2.val:
                store = pointer1.next
                
                if pointer1.next is not None and pointer1.next.val <= pointer2.val:
                    # pointer1.next.next = pointer2
                    pass
                else:
                    pointer1.next = pointer2
                
                previous_node = pointer1
                pointer1 = store
                         
            else:
                store = pointer2.next
                
                if pointer2.next is not None and pointer2.next.val <= pointer1.val:
                    # pointer2.next.next = pointer1
                    pass
                else:
                    pointer1.next = pointer2
                
                previous_node = pointer2
                pointer2 = store
        

        return result
        
          
def traverse(head: ListNode):
    cur_node = head
    while cur_node is not None:
        print(cur_node.val)
        cur_node = cur_node.next
             
# list1 = [1, 3, 4]
# lsit2 = [1,2,4]
# desired output [1,2，3,4，4]

node13 =ListNode(4,None)
node12=ListNode(3,node13)
node11=ListNode(1,node12)

head2=node11


node23=ListNode(4, None)
node22=ListNode(2,node23)
node21=ListNode(1.5,node22)
head1=node21
        
e1=Solution()
r1=e1.mergeTwoLists(head1, head2)
traverse(r1)




        
                    
        
        

                






