from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    """ 
    Write a program that takes an array denoting the daily stock price, 
    and returns the maximum profit that could be made by buying and then 
    selling one share of that stock

    have: prices - list of stock prices

    logic:
        * we instantiate our result variable for return.
        * brute force * give an n*n traversal of linear double loop to capture
            maximum difference.

        * we approach a linear traversal
        * keep the current minimum within scope
        * when we see a number greater than, we take the difference and apply to profit seen.
        * when we enounter a number less than, we replace the minimum and continue.
    """

    max_profit_seen = 0.0

    current_minimum = float("inf")

    for idx, stock_price in enumerate(prices):
        max_profit_seen = max(max_profit_seen, stock_price-current_minimum)
        current_minimum = min(current_minimum, stock_price)

    return max_profit_seen


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
