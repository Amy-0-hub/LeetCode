# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cur_node = head
        count = 0
        list1= []
        while cur_node is not None:
            list1.append(cur_node.val)
            cur_node = cur_node.next
            count += 1
        result = 0
        for i in range(count):
            result += list1[i] * ( 2 ** (count-1-i))

        return result


            


node4 = ListNode(1, None)
node3 = ListNode(1, node4)
node2 = ListNode(0, node3)
node1 = ListNode(1, node2)        
head1 = node1

e1 = Solution()
r1 = e1.getDecimalValue(head1)
print(r1)
        



# 101 -> 5=1* 2^2 + 0 * 2^1 + 1*2^0
# 1011 ->  1* 2^3 + 0* 2^2 + 1 * 2^1  + 1 * 2^0 = 11      count = 4, 
          

  