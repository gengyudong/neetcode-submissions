"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if not node:
                return None
            
            if node in visited:
                return visited[node]
            
            cloneNode = Node(node.val)
            visited[node] = cloneNode

            for neighbor in node.neighbors:
                cloneNode.neighbors.append(dfs(neighbor))
            
            return cloneNode
        
        return dfs(node)
