from solution import Solution


def test_solution():
    examples = [
        {
            "input": ["PAYPALISHIRING", 3],
            "output": "PAHNAPLSIIGYIR",
        },
        {
            "input": ["PAYPALISHIRING", 4],
            "output": "PINALSIGYAHRPI",
        },
        {
            "input": ["A", 1],
            "output": "A",
        },
    ]

    for example in examples:
        assert Solution().convert(*example["input"]) == example["output"]
