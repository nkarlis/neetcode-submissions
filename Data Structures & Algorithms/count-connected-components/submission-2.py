class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visit = [False] * n
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
           

        count = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                count += 1
        return count

        