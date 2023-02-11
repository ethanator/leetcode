from solution import Solution


def test_solution():
    examples = [
        {
            "input": [[1, 5, 0, 3, 5]],
            "output": 3,
        },
        {
            "input": [[0]],
            "output": 0,
        },
    ]

    for example in examples:
        assert Solution().minimumOperations(*example["input"]) == example["output"]
