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
             # 1. Check if there are at least k nodes left to reverse
            cursor = groupPrev
            for _ in range(k):
                cursor = cursor.next
                if not cursor:
                    return dummy.next
            # 2. Setup pointers for the current k-group reversal
            prev = cursor.next
            cur = groupPrev.next
            # 3. Reverse the k nodes            
            for _ in range(k):
                nxt = cur.next 
                cur.next = prev
                prev = cur
                cur = nxt
            # 4. Connect the reversed group back to the main list
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
        return dummy.next   