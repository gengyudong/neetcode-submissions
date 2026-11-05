class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island_num = 0

        def bfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0" or
                (r, c) in visited):
                return
            
            visited.add((r, c))

            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r + 1, c)
            bfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    island_num += 1
        
        return island_num
        