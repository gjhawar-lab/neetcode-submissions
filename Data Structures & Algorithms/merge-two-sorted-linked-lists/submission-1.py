# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (e.g., empty lists)
        dummy = ListNode()
        curr = dummy  # 'curr' will be the tail of the new list

        # While both lists still have nodes, compare and pick the smaller one
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1      # attach the smaller node
                list1 = list1.next     # advance list1
            else:
                curr.next = list2      # attach list2's node (tie goes to list2)
                list2 = list2.next     # advance list2
            curr = curr.next           # move tail pointer forward

        # At this point, one list is exhausted.
        # Attach the remaining nodes of the non-empty list (if any).
        curr.next = list1 if list1 else list2

        # Return the head of the merged list (skip the dummy node)
        return dummy.next