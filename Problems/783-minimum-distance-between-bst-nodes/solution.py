import sys
from tree import TreeNode
from typing import Optional


class Solution:
    min_diff = sys.maxsize
    prev_node = None

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.inOrderTraversal(root)
        return self.min_diff

    def inOrderTraversal(self, node: Optional[TreeNode]) -> int:
        if not node: return

        self.inOrderTraversal(node.left)

        if self.prev_node:
            self.min_diff = min(self.min_diff, node.val - self.prev_node.val)

        self.prev_node = node

        self.inOrderTraversal(node.right)
