# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
        cur, prev = slow.next, None
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        first, second = head, prev
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2