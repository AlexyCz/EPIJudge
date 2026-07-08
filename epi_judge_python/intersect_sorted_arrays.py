from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    """
        We have two sorted arrays; let us return a sorted deduplicated array.

        Have:
            A, which is a list of integers;
            B, which is also a list of integers.

        Logic:
            Hint given points us to think about list magnitudes and using that
            to our advantage.

            * Quick and simple: create a python set object for both and intersect with
                arithmetic op &. Set comprehension runs for both too to be succint.
                ! Does not retain order, only uniqueness ! Use sort(); O(nLogn).
            * One pass, take the longer one and iterate across it.
            * create new list instance.
            * at each index, we take the smaller of the two and only if it is not equal
                to the most recent value in our result list.
            * go until the end of both; once the index is out of range for the smaller we skip
                and only account for the larger list for value checks.
    """
    return sorted(list(
        {a for a in A} &
        {b for b in B}
    ))

    # last_index_B, last_index_A = len(B) - 1, len(A) - 1

    # current_index_B, current_index_A = 0, 0

    # result = []

    # if last_index_B > last_index_A:
    #     last_index_A, last_index_B = last_index_B, last_index_A

    # while current_index_A <= last_index_A:
    #     if current_index_B <= last_index_B:
    #         current_b_value = B[current_index_B]

    #     current_a_value = A[current_index_A]

    #     if current_a_value > current_b_value and current_b_value != result[-1]:
    #         result.append(current_b_value)
    #         current_index_B += 1
    #     elif current_a_value < current_b_value and current_a_value != result[-1]:
    #         result.append(current_a_value)
    #         current_index_A += 1
    #     elif current_a_value != result[-1]:
    #         result.append(current_a_value)
    #         current_index_A += 1
    #         current_index_B += 1
    #     else:
    #         current_index_A += 1
    #         current_index_B += 1

    # return result
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
