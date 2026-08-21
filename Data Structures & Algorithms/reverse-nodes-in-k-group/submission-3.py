# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            cursor = groupPrev
            for _ in range(k):
                cursor = cursor.next
                if not cursor:
                    return dummy.next
            cur = groupPrev.next
            prev = cursor.next
            for _ in range(k):
                nxt = cur.next
                cur.next = prev 
                prev = cur
                cur = nxt
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
