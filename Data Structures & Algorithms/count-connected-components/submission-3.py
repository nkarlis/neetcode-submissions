class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visit = [False] * n

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            for nei in adj[node]:
                if visit[nei] != True:
                    visit[nei] = True
                    dfs(nei)


        
        count = 0
        for i in range(n):
            if visit[i] == False:
                visit[i] = True
                dfs(i)
                count+=1

        return count