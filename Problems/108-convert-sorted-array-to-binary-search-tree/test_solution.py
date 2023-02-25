from solution import Solution
from tree import build_tree, compare_tree


def test_solution():
    examples = [
        {
            "input": [-10, -3, 0, 5, 9],
            "output": [
                [0,  -3, 9,  -10, None,    5],
                [0, -10, 5, None,   -3, None, 9],
            ],
        },
        {
            "input": [1, 3],
            "output": [
                [3,    1],
                [1, None, 3],
            ],
        },
    ]

    for example in examples:
        actual_tree = Solution().sortedArrayToBST(example["input"])
        assert any(compare_tree(actual_tree, build_tree(example_output)) for example_output in example["output"])
