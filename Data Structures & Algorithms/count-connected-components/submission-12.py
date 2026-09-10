class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # if len(edges) > n - 1:
        #     return False
        adj = [[] for i in range(n)]
        visit = [False] * n
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            for nei in adj[node]:
                if visit[nei] == False:
                    visit[nei] = True
                    dfs(nei)


        count = 0
        for node in range(n):
            if visit[node] == False:
                visit[node] = True
                dfs(node)
                count += 1
        return count

        