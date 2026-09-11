"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToCopy = {None : None}
        def dfs(node):
            if node in oldToCopy:
                return oldToCopy[node]
            oldToCopy[node] = Node(node.val)
            for nei in node.neighbors:
                oldToCopy[node].neighbors.append(dfs(nei))
            return oldToCopy[node]
        dfs(node)
        return oldToCopy[node]