class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = [False] * n
        comp = 0
        def dfs(node):
            for nei in adj[node]:
                if visit[nei] == False:
                    visit[nei] = True
                    dfs(nei)
            
        for node in range(n):
            if visit[node] == False:
                visit[node] = True
                dfs(node)
                comp += 1
        return comp
        