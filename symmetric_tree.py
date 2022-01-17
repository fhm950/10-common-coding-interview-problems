"""
Check whether the Binary Tree is symmetric or not.
Given a binary tree root, check if it's symmetric around
its center (a mirror of itself)
"""

def are_symmetric(root_1, root_2):
    if root_1 is None and root_2 is None:
        return True
    elif ((root_1 is None) != (root_2 is None) or root_1.val != root_2.val):
        return False
    else:
        return are_symmetric(root_1.left, root_2.right) and are_symmetric(root_1.right, root_2.left)


def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)


if __name__ == '__main__':
    is_symmetric()