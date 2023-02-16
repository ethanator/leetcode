from solution import Solution


def test_solution():
    examples = [
        {
            "input": ["III"],
            "output": 3,
        },
        {
            "input": ["LVIII"],
            "output": 58,
        },
        {
            "input": ["MCMXCIV"],
            "output": 1994,
        },
    ]

    for example in examples:
        assert Solution().romanToInt(*example["input"]) == example["output"]
