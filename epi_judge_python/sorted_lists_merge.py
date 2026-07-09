from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    """
        We have two linked lists, sorted, and we want to return the
        resulting merge of the two.

        Have:
            L1 and L2 linked lists, which have attributes `data` (int) 
                and `next` (ListNode).

        Logic:
            - Either of the two can be None, given the Optional[].
            - Best case, one is None and we only need to acknowledge the
                other.
            - Most likely, one is longer than the other, less likely they're
                equal.

            * Instantiate a new sentinal ListNode to have as result pointer.
            * Start a while loop that exits when we exhaust either of the two
                lists, i.e. either of the two current node states is None.
            * Begin comparison of current nodes: if L1's current node is lesser,
                add it as next to result list; vice versa for L2 if lesser.
            * Transition to next node via the `next` attr of node that was used.
            * Once out of while loop, check for non-null node and simply attach
                to sentinal list to complete the merge.
            * Return sentinal linked list.
            .
    """
    result = ListNode()
    current_state = result

    while L1 and L2:
        if L1.data < L2.data:
            current_state.next = L1
            L1, current_state = L1.next, current_state.next
        else:
            current_state.next = L2
            L2, current_state = L2.next, current_state.next

    if L1:
        current_state.next = L1

    if L2:
        current_state.next = L2

    return result.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
