from typing import Tuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def recurse(node: BinaryTreeNode, height: int) -> Tuple:
    if not node:
        return -1, True

    left_height, left_balanced = recurse(node.left, height)
    right_height, right_balanced = recurse(node.right, height)

    if all([left_balanced, right_balanced, (abs(left_height-right_height) < 2)]):
        return max(left_height, right_height) + 1, True

    return max(left_height, right_height) + 1, False


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    """
    Write a program that takes as input the root of a binary tree and
    checks whether the tree is height-balanced.

    have: variable `tree` of type BinaryTreeNode(data, left, right)

    logic:
        key point: a height balanced tree equates to a tree whose left
                    and right subtrees' difference in height cannot
                    exceed one.

        * recursive traversal
        * base cases: if node is none, return tuple of -1, True
        * recurse left with current_node.left, assign returned value to left_height, left_balanced
        * recurse right with current_node.right, assign returned value to right_height, right_balanced
        * we need all() to be valid with the three following inputs: left_balanced, right_balanced, abs(left_height-right_height)
            * if satisfied, return max of the two heights + 1, to include current level, and True
        * if not all satisfied, we return the max of the two heights and False
    """
    _, result = recurse(tree, 0)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
