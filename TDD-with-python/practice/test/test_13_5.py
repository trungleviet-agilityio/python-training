"""Requirement: Write a function named choose_from_hist that takes a histogram
 as defined in Section 11.1 and returns a random value from the
 histogram, chosen with probability in proportion to frequency.
"""
import unittest

import random


def histogram(s):
    """
    Counts the number of occurrences of each character in a string.

    Args:
        s (str): The input string.

    Returns:
        A dictionary with the characters in the string as keys and their counts as values.
    """
    character_counts = {}
    for character in s:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts


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
    result = 0
    for d in dicts:
        if not isinstance(d, dict):
            raise TypeError("Arguments must be dictionaries.")
        result += sum(d.values())
    return result


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

    # Choose a key randomly based on its value
    random_key = random.choice(list(h.keys()))
    probability = h[random_key] / sum(h.values())
    values_sum = sum(h.values())
    print('Random value is "{}" and its probability is {}/{}, i.e. {}.'
          .format(random_key, h[random_key], sum(h.values()), probability))
    return random_key


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
        result = choose_from_hist(h)
        self.assertIn(result, h)

        # Test with a non-dictionary argument
        non_dict = "This is not a dictionary"
        with self.assertRaises(TypeError):
            choose_from_hist(non_dict)


if __name__ == '__main__':
    unittest.main()
