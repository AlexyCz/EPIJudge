import collections

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    """
        Write a program which takes text for a letter and text for a 
            magazine and determines if it is possible to write the letter
            using the magazine.

        Have:
            letter_text, string of characters to attempt finding completely in
                the magazine
            magazine_text, a source character bank to attempt finding every
                character in the letter

        Logic:
            * dictionary is best ds; use it to create counters
                - use collections.Counter()
            * once we have a Counter obj for both strings, we can attempt arithmetic
                difference between the two dictionaries.
            * Doing subtraction [subtract() method] across Counter objects keeps positive values, i.e.
                if we have magazine counts as left operand, a true response would
            * We can brute force check across all letter chars, any negative count is false.
            * return True if we address all chars without negative counts.
            ---
            post docs read: inclusion check via <= between two counter objects where left hand operand
                value must be less than or equal to right hand operand value to be included, i.e. True.
    """
    letter_counter, magazine_counter = collections.Counter(letter_text), collections.Counter(magazine_text)

    # use magazine_counter as source, so left hand operand for subtract method
    if not letter_counter <= magazine_counter:
        return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
