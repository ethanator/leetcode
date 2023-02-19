from solution import Solution
from tree import build_tree


def test_solution():
    examples = [
        {
            "input": [4, 2, 6, 1, 3],
            "output": 1,
        },
        {
            "input": [1, 0, 48, None, None, 12, 49],
            "output": 1,
        },
    ]

    for example in examples:
        root = build_tree(example["input"])
        assert Solution().minDiffInBST(root) == example["output"]
