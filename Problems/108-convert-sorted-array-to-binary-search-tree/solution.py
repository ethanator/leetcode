from tree import TreeNode
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.buildBST(0, len(self.nums) - 1)

    def buildBST(self, start_index: int, end_index: int) -> Optional[TreeNode]:
        if start_index > end_index: return None
        mid = (start_index + end_index) // 2
        return TreeNode(
            self.nums[mid],
            self.buildBST(start_index, mid - 1),
            self.buildBST(mid + 1, end_index),
        )