from solution import Solution


def test_solution():
    examples = [
        {
            "input": [[1, 2, 0, 0], 34],
            "output": [1, 2, 3, 4],
        },
        {
            "input": [[2, 7, 4], 181],
            "output": [4, 5, 5],
        },
        {
            "input": [[2, 1, 5], 806],
            "output": [1, 0, 2, 1],
        },
        {
            "input": [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1],
            "output": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        },
    ]

    for example in examples:
        assert Solution().addToArrayForm(*example["input"]) == example["output"]
