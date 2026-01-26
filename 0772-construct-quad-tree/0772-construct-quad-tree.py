# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        stack = [(0, 0, n)]  # (top, left, length)
        result = {}  # maps (top, left, length) -> Node

        while stack:
            top, left, l = stack[-1]

            if l == 1:
                stack.pop()
                result[(top, left, l)] = Node(grid[top][left], True)
                continue

            half = l // 2
            quads = [
                (top, left, half),
                (top, left + half, half),
                (top + half, left, half),
                (top + half, left + half, half)
            ]

            all_ready = True
            for q in quads:
                if q not in result: 
                    all_ready = False

            if all_ready:
                stack.pop()
                nodes = [result[q] for q in quads]
                if all(n.isLeaf and n.val == nodes[0].val for n in nodes):
                    result[(top, left, l)] = Node(nodes[0].val, True)
                else:
                    result[(top, left, l)] = Node(0, False, *nodes)
            else:
                for q in quads:
                    if q not in result:
                        stack.append(q)

        return result[(0, 0, n)]
