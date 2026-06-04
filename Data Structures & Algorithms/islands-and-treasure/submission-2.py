class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))


        def addCell(r, c):
            if( r not in range(rows) or c not in range(cols) or (r,c ) in visit
                or grid[r][c] == -1           
            ):
                return
            q.append((r, c))
            visit.add((r,c))

        dist = 0
        while q:
            
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
                grid[r][c] = dist

            dist +=1
