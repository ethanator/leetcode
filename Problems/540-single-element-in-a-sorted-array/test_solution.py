import random
from solution import Solution


def test_solution(
        total_tests: int = 100,
        min_nums_length: int = 1,
        max_nums_length: int = 10000,
        min_num: int = 0,
        max_num: int = 10000
    ) -> None:
    for _ in range(total_tests):
        nums_length = random.randint(min_nums_length, max_nums_length)
        if nums_length % 2 == 0: nums_length += 1

        nums = []
        for _ in range((nums_length + 1) // 2):
            num = random.randint(min_num, max_num)
            while num in nums:
                num = random.randint(min_num, max_num)
            nums.append(num)

        nums = sorted(nums)
        single_index = random.randint(0, len(nums) - 1)
        nums = [
            num
            for l in [
                [num] if i == single_index else [num, num]
                for i, num in enumerate(nums)
            ]
            for num in l
        ]
        assert len(nums) == nums_length
        single_index = single_index * 2

        assert Solution().singleNonDuplicate(nums) == nums[single_index]
