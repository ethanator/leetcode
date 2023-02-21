from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1

        while l < h:
            m = l + (h - l) // 2
            if m % 2 == 1: m -= 1
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                h = m

        return nums[l]