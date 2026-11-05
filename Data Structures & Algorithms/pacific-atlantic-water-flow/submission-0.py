from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                
                if (r, c) in visited:
                    continue
                
                visited.add((r, c))

                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited):
                        continue
                    
                    if heights[nr][nc] >= heights[r][c]:
                        queue.append((nr, nc))

        # Initialize queues with border & bfs
        pacific_queue = deque()
        atlantic_queue = deque()

        for r in range(rows):
            pacific_queue.append((r, 0))
            atlantic_queue.append((r, cols - 1))

        for c in range(cols):
            pacific_queue.append((0, c))
            atlantic_queue.append((rows - 1, c))

        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)

        # Find intersection
        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    result.append([r,c])
        
        return result