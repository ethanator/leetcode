from collections import deque
from tree import TreeNode
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([(root, 0)])
        order = []

        while len(q) > 0:
            node, depth = q.pop()
            if len(order) <= depth: order.append(deque())
            if depth % 2 == 0:
                order[depth].append(node.val)
            else:
                order[depth].appendleft(node.val)
            if node.left: q.appendleft((node.left, depth + 1))
            if node.right: q.appendleft((node.right, depth + 1))

        return [list(level) for level in order]