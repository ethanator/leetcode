# problem413.py
# 
# 413. Arithmetic Slices
# https://leetcode.com/problems/arithmetic-slices/
#
# Author: Yuxuan Chen
# Date: February 18, 2021

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        prev_diff = None
        counter = 1
        slices = 0
        for i in range(1, len(A)):
            diff = A[i] - A[i - 1]
            if diff == prev_diff:
                counter += 1
            else:
                if counter >= 2:
                    slices += counter * (counter - 1) // 2
                counter = 1
            prev_diff = diff
        if counter >= 2:
            slices += counter * (counter - 1) // 2
        return slices
