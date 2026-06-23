class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            grid[row][col] = '0'

            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc                        

                    if (0 <= r < rows) and (0 <= c < cols) and (grid[r][c] == '1'):
                        q.append((r,c))
                        grid[r][c] = '0'
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    bfs(row, col)
                    islands += 1
        
        return islands