# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Step 1 : find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None

        # Step 2 : reverse 2nd half
        head_for_second_half = self.reverse_list(middle)

        # Step 3 : merge the 2 lists
        self.merge_two_lists(head, head_for_second_half, middle)


    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # save before we break the link
            curr.next = prev     # reverse this arrow
            prev = curr
            curr = nxt

        return prev


    def merge_two_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode], middle: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        val = 1
        while list1 and list2 and list1 != middle:
            if val == 1:
                curr.next = list1
                list1 = list1.next
                val = 2
            else:
                curr.next = list2
                list2 = list2.next
                val = 1

            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next
        