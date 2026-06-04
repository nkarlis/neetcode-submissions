class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1, 0], [-1,0], [0,1], [0,-1]]

        total = 0
        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    if( (r+dr)  in range(rows) and (c+dc)  in range(cols)
                        and grid[r+dr][c+dc] ==1
                    ):
                        grid[r+dr][c+dc] = 2
                        q.append((r+dr, c+dc))
                        fresh -=1

            total +=1

        return total if fresh == 0 else -1

                    

