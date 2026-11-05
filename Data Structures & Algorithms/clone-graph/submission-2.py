"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        visited = {}
        visited[node] = Node(node.val)
        queue = deque()
        queue.append(node)

        while queue:
            current_node = queue.popleft()

            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    clone_node = Node(neighbor.val)
                    visited[neighbor] = clone_node
                    queue.append(neighbor)

                visited[current_node].neighbors.append(visited[neighbor])
        
        return visited[node]
