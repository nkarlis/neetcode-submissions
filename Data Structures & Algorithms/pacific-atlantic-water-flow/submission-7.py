class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()


        def dfs(r, c, visit, prev):
            if( r not in range(ROWS) or c not in range(COLS) or 
            (r, c) in visit or heights[r][c] < prev):
                return
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS - 1, atl, -1)


        for c in range(COLS):
            dfs(0, c, pac,  -1)
            dfs(ROWS - 1, c, atl , -1)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r, c])
        return res