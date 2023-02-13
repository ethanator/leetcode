from solution import Solution


def test_solution():
    examples = [
        {
            "input": [3, 7],
            "output": 3,
        },
        {
            "input": [8, 10],
            "output": 1,
        },
    ]

    for example in examples:
        assert Solution().countOdds(*example["input"]) == example["output"]
