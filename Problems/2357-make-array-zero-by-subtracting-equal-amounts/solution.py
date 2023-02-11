from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = {}
        count = 0

        for num in nums:
            if not num in d:
                d[num] = True
                count += 1

        return count - 1 if 0 in d else count