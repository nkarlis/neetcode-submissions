class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # not free
        # O(E+V)

        # not loop, all nodes must be connected
        # dfs visit all nodes, if len(visit) == n True else False
        # because it is undirected we should try not to count each edge twice
        # add value prev, the previous node we visited

        if not n:
            return True
        visit, cycle = set(), set()
        adj = {i:[] for i in range(n)}
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)

            for j in adj[i]:
                if j == prev:
                    continue

                if not dfs(j, i):
                    return False

            return True

        if not dfs(0, -1):
            return False
        return True if len(visit) == n else False