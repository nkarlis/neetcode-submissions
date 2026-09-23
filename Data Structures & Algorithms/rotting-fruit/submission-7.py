class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        while fresh and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dir:
                    curRow, curCol = r + dr, c + dc
                    if( curRow in range(ROWS) and curCol in range(COLS) 
                    and grid[curRow][curCol] == 1):
                        fresh -= 1
                        grid[curRow][curCol] = 0
                        q.append((curRow,curCol))
            time += 1
        return time if fresh == 0 else -1