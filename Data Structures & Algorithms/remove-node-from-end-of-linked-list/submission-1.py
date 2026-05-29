# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a dummy node in case the Head node needs to be removed
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy
        
        # Move fast pointer n steps ahead to create n-node gap
        for i in range(n):
            fast = fast.next
        
        # Move both pointers until fast reaches end
        # When fast is at last node, slow will be at node before target
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from end by skipping it
        slow.next = slow.next.next
        
        return dummy.next  # Return head of modified list
