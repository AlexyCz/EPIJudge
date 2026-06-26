import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    """
        Given two nodes in a binary tree, design an algorithm that computes
            their lca; assume that each node has a parent pointer.

        have:
            node 0 and node 1 of type BinaryTreeNode with value, left, right, parent attrs.

        logic:
            * base case being if either is the root where parent is none will be the lca.
            ---
            * we have a hint of depth providing easy backtrack to lca via parent pointer.
            ---
            * idea! depth-first to find shortest path to node0 and node1.
                * the trail to one will stop overlapping with the other the moment we drop
                    into the node right after the lca.
                * space is at most O(k) where k is depth of tree.
    """
    trail = list()

    def depth_first_trail_from(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        nonlocal trail
        print(f"\n node:{node}, trail:{trail}")

        if not node:
            return

        if node.data in trail:
            return node

        trail.append(node.data)
        _ = depth_first_trail_from(node.parent)
        
        return

    _ =  depth_first_trail_from(node0)

    result = depth_first_trail_from(node1)

    return result


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
