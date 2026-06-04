"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyToOld = {None:None}
        cur = head

        while cur:
            copy = Node(cur.val)
            copyToOld[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copy = copyToOld[cur]
            copy.next = copyToOld[cur.next]
            copy.random = copyToOld[cur.random]
            cur = cur.next
        return copyToOld[head]

        