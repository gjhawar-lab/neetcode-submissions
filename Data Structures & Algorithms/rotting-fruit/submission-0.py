class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        FRESH  = 1
        ROTTEN = 2
        DIRS   = [(1,0),(-1,0),(0,1),(0,-1)]

        rows, cols = len(grid), len(grid[0])

        # seed queue with every rotten cell; count fresh ones
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ROTTEN:
                    queue.append((r, c))
                elif grid[r][c] == FRESH:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0

        while queue and fresh > 0:
            minutes += 1
            for i in range(len(queue)):       # one BFS level = one minute
                r, c = queue.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN
                        fresh -= 1
                        queue.append((nr, nc))

        return minutes if fresh == 0 else -1