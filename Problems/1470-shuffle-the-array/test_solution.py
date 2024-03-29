from solution import Solution


def test_solution():
    examples = [
        {
            "input": [[2, 5, 1, 3, 4, 7], 3],
            "output": [2, 3, 5, 4, 1, 7],
        },
        {
            "input": [[1, 2, 3, 4, 4, 3, 2, 1], 4],
            "output": [1, 4, 2, 3, 3, 2, 4, 1]
        },
        {
            "input": [[1, 1, 2, 2], 2],
            "output": [1, 2, 1, 2],
        },
    ]

    for example in examples:
        assert Solution().shuffle(*example["input"]) == example["output"]
