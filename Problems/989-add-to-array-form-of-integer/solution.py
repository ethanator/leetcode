from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_pointer = len(num) - 1
        carry_over = 0

        while k > 0 or carry_over > 0:
            tmp = num[num_pointer] + (k % 10) + carry_over
            num[num_pointer] = tmp % 10
            carry_over = tmp // 10
            k //= 10
            num_pointer -= 1

            if num_pointer < 0 and (k > 0 or carry_over > 0):
                num = [0] + num
                num_pointer = 0
        if carry_over > 0:
            num[0] = carry_over

        return num