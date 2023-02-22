"""Requirement: Write a function named choose_from_hist that takes a histogram
 as defined in Section 11.1 and returns a random value from the
 histogram, chosen with probability in proportion to frequency.
"""
import unittest

import random
from collections import defaultdict


def histogram(s):
    """
    Counts the number of occurrences of each character in a string.

    Args:
        s (str): The input string.

    Returns:
        A dictionary with the characters in the string as keys and their counts as values.
    """
    character_counts = defaultdict(int)
    for character in s:
        character_counts[character] += 1
    return dict(character_counts)


def sum_dict_values(*dicts):
    """
    Sums the values of all the keys in one or more dictionaries.

    Args:
        *dicts: One or more dictionaries to be summed.

    Returns:
        The total sum of all the values in all the dictionaries.

    Raises:
        TypeError: If any of the input arguments are not dictionaries.
    """
    if not all(isinstance(d, dict) for d in dicts):
        raise TypeError("All arguments must be dictionaries.")

    return sum(value for d in dicts for value in d.values())


def choose_from_hist(h):
    """
    Randomly selects a key from a dictionary based on the values of the keys.

    Args:
        h (dict): A dictionary with keys and integer values.

    Returns:
        A randomly selected key from the dictionary.
    """
    if not isinstance(h, dict):
        raise TypeError("Argument must be a dictionary")

    # Unpack the keys and values of the dictionary into two separate tuples
    keys, weights = zip(*h.items())

    # Use random.choices with the weights argument to select a key based on its value
    return random.choices(keys, weights=weights)[0]


class TestHistogram(unittest.TestCase):
    def test_empty_input(self):
        # Test histogram with empty input
        result = histogram("")
        self.assertEqual(result, {})

    def test_single_char_input(self):
        # Test histogram with a single character input
        result = histogram("a")
        self.assertEqual(result, {'a': 1})

    def test_multi_char_input(self):
        # Test histogram with a multi-character input
        result = histogram("hello")
        self.assertEqual(result, {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_sum_dict_values(self):
        # Test function that sums values of a variable number of dictionaries
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        result = sum_dict_values(d1, d2)
        self.assertEqual(result, 10)

    def test_choose_from_hist(self):
        # Test function that selects a key randomly from a dictionary based on its value
        # Test with a valid histogram
        h = {'a': 1, 'b': 2, 'c': 3}
        results = []
        n_trials = 10000
        for i in range(n_trials):
            result = choose_from_hist(h)
            results.append(result)
        counts = {k: results.count(k) for k in h}
        expected_counts = {k: int(n_trials * v / sum(h.values())) for k, v in h.items()}
        for k in h:
            self.assertAlmostEqual(counts[k], expected_counts[k], delta=0.02 * n_trials)


if __name__ == '__main__':
    unittest.main()
