class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visit = [False] * n

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        def dfs(node):
            if visit[node] == False:
                visit[node] = True
                for nei in adj[node]:
                    dfs(nei)

        count = 0
        for node in range(n):
            if visit[node] == False:
                visit[node] = True
                count+=1
                for nei in adj[node]:
                    dfs(nei)
        return count
                    
                