import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    """
        Trade is encoded as: 123111, AAPL, 30, 456.12
        trade[0] - milliseconds since start of day.
        trade[1] - symbol
        trade[2] - share number
        trade[3] - price

    Write a program that takes as input a set of sorted sequences and 
        computes the union of these sequences as a sorted sequence.
        e.g. [3,5,7], [0,6], [0,6,28] -> [0,0,3,5,6,6,7,28]

    have: a list of lists containing numbers; already sorted.

    logic:
        * use a heap (heapq.heapify(iterable)) initialized at empty.
        * linear traversal
        * each item encountered will be passed into heappush(),
            along with our result heap.
        * return result
    """ 
    
    # return list(heapq.merge(*sorted_arrays))  # pythonic.
    merged_sequences = list()
    heapq.heapify(merged_sequences)

    for seq in sorted_arrays:
        for n in seq:
            heapq.heappush(merged_sequences, n)

    return heapq.nsmallest(len(merged_sequences), merged_sequences)
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
