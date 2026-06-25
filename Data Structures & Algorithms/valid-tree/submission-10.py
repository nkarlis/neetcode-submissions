class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 > n:
            return False
        adj = [[] for i in range(n)]
        visit = set()
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if prev == nei:
                    continue
                if nei not in visit:
                    dfs(nei, node)
            return True
        
        return dfs(0, -1) and len(visit) == n