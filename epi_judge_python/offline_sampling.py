import functools
import random
import time
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def random_sampling(k: int, A: List[int]) -> None:
    """
        Implement algorithm that takes as input an array of distinct elements 
            and a size, and returns a subset of the given size of the array 
            of elements. All subsets should be equally likely.
        Return the result in input array itself.
    """
    random.seed(time.monotonic_ns())
    chosen_idx = set()

    while len(chosen_idx) < k+1:
        chosen_idx.add(random.randrange(0, len(A)))

    for idx, choice in enumerate(chosen_idx):
        A[idx], A[choice] = A[choice], A[idx]

    return 


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))] for a in result],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('offline_sampling.py',
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
