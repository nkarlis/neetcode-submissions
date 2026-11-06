# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first, second = head, head.next
        while second and second.next:
            first = first.next
            second = second.next.next
        cur = first.next
        first.next = None
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        l1, l2 = head, prev
        while l2:
            nxt1, nxt2 = l1.next, l2.next
            l1.next = l2
            l2.next = nxt1
            l1, l2 = nxt1, nxt2

