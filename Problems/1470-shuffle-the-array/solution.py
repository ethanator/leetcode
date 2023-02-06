from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [j for i in range(n) for j in [nums[i], nums[i + n]]]
