from test_framework import generic_test


def reverse(x: int) -> int:
    """
        Write a program which takes an integer and returns the integer corresponding 
        to the digits of the input written in reverse order. e.g. 42 -> 24, -314 -> -413.

        Hint: How would you solve the same problem if the input is presented as a string?
    """

    # check sign
    sign = 1
    reversedInt = 0

    if x < 0:
        sign = -1
        x *= sign

    while x:
        reversedInt *= 10
        reversedInt += (x % 10)
        x //= 10

    return reversedInt * sign


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
