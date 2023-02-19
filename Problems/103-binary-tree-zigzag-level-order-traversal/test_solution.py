from solution import Solution
from tree import build_tree
from typing import List


def test_solution():
    examples = [
        {
            "input": [3, 9, 20, None, None, 15, 7],
            "output": [[3], [20, 9], [15, 7]],
        },
        {
            "input": [1],
            "output": [[1]],
        },
        {
            "input": [],
            "output": [],
        },
    ]

    for example in examples:
        root = build_tree(example["input"])
        assert Solution().zigzagLevelOrder(root) == example["output"]
