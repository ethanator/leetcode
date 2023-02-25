from typing import List, Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(val_list: List[int]) -> TreeNode:
    if len(val_list) == 0: return None
    node_list = []

    for i, val in enumerate(val_list):
        node = TreeNode(val) if not val is None else None
        node_list.append(node)
        if i == 0 or not val: continue
        parent_idx = (i - 1) // 2
        if i % 2 == 1:
            node_list[parent_idx].left = node
        else:
            node_list[parent_idx].right = node

    return node_list[0]

def compare_tree(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if not root1:
        if not root2: return True
        return False
    if not root2: return False
    if root1.val != root2.val: return False
    return (
        compare_tree(root1.left, root2.left) and
        compare_tree(root1.right, root2.right)
    )