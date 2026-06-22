import collections

from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    """
    Write a program to test whether the letters forming a string can be permuted
        to form a palindrome.

    have: a string named `s`

    logic:
        * quantify character counts
            * can use collections.Counter()
        * for a string to be permutable to a palindrome, we need all evens
            or all evens and a single odd. The odd satisfies the single middle
            character.
        * we instantiate an `odd` flag to initialize as false, and set to true
            the moment we encounter an odd count character from the dictionary.
            * if we encounter another odd, we return False.
        * we loop throught the hash items, and modulo counts with 2 for even value
            validation.
        * return true if we loop through everything.
    """
    odd_count_char = False
    character_counts = collections.Counter(s)

    for _, count in character_counts.items():
        parity = count % 2

        if odd_count_char and parity:
            return False

        if parity and not odd_count_char:
            odd_count_char = True

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
