# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv, cur = None, head
        while cur:
            nxt = cur.next  # temporarily save where to iterate next
            cur.next = prv  # reverse the link (from prv -> cur to cur -> prv)
            prv, cur = cur, nxt  # update the pointers for next iteration
        return prv