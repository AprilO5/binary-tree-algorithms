from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Return the maximum number of nodes from the root to the deepest leaf.
    An empty tree has a depth of 0.
    """
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Return the lowest node in a BST that has both p and q as descendants.
    A node can be its own ancestor, so this also handles cases where p or q
    is the root or is an ancestor of the other node.
    """
    if root is None:
        return None

    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    return root
