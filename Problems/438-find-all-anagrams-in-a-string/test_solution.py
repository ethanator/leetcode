from solution import Solution


def test_solution():
    examples = [
        {
            "input": ["cbaebabacd", "abc"],
            "output": [0, 6],
        },
        {
            "input": ["abab", "ab"],
            "output": [0, 1, 2],
        },
    ]

    for example in examples:
        assert Solution().findAnagrams(*example["input"]) == example["output"]
