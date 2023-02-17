from solution import Solution, TreeNode
from typing import List


def build_tree(val_list: List[int]) -> TreeNode:
    node_list = []

    for i, val in enumerate(val_list):
        node = TreeNode(val) if val else None
        node_list.append(node)
        if i == 0 or not val: continue
        parent_idx = (i - 1) // 2
        if i % 2 == 1:
            node_list[parent_idx].left = node
        else:
            node_list[parent_idx].right = node

    return node_list[0]

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
