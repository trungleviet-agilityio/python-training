"""Requirements: Write a function called is_abecedarian that returns True
if the letters in a word appear in alphabetical order
(double letters are ok). How many abecedarian words are there?
"""

import unittest
from unittest.mock import MagicMock

# Check if a word is abecedarian
def is_abecedarian(word):
    """
    Function to check if a word if it is made up from characters in the alphabet consecutively,
    that is, from a,b,c etc.

    Parameters:
    word (string): Word to test

    Returns:
    bool: True if word is composed of characters in alphabetical order
    """
    return list(word.lower()) == sorted(word.lower())


class TestIsAbecedarian(unittest.TestCase):

    def test_is_abecedarian_true(self):
        # Test cases where the word is abecedarian
        self.assertTrue(is_abecedarian("abc"))
        self.assertTrue(is_abecedarian("aberr"))
        self.assertTrue(is_abecedarian("abhor"))
        self.assertTrue(is_abecedarian("ghosty"))

    def test_is_abecedarian_false(self):
        # Test cases where the word is not abecedarian
        self.assertFalse(is_abecedarian("cba"))
        self.assertFalse(is_abecedarian("bdea"))
        self.assertFalse(is_abecedarian("zoo"))
        self.assertFalse(is_abecedarian("keyboard"))

    def test_is_abecedarian_with_mock(self):
        # Test case that uses a mock object to simulate the sorted function
        mock_list = MagicMock(return_value=["a", "b", "c", "d"])
        with unittest.mock.patch('builtins.sorted', mock_list):
            self.assertTrue(is_abecedarian("abcd"))

    def test_is_abecedarian_single_letter(self):
        # Test cases with single-letter words
        self.assertTrue(is_abecedarian("a"))
        self.assertTrue(is_abecedarian("b"))
        self.assertTrue(is_abecedarian("z"))

    def test_is_abecedarian_repeated_letters(self):
        # Test cases with repeated letters
        self.assertTrue(is_abecedarian("aa"))
        self.assertTrue(is_abecedarian("bb"))
        self.assertTrue(is_abecedarian("zz"))
        self.assertTrue(is_abecedarian("abbbcccd"))
        self.assertFalse(is_abecedarian("dddeeebbb"))
        self.assertTrue(is_abecedarian("abcdd"))

    def test_is_abecedarian_capital_letters(self):
        # Test cases with words with mixed capitalization
        self.assertTrue(is_abecedarian("Abc"))
        self.assertTrue(is_abecedarian("abC"))
        self.assertTrue(is_abecedarian("ABC"))
        self.assertTrue(is_abecedarian("ABCD"))
        self.assertFalse(is_abecedarian("Acb"))

    def test_is_abecedarian_numbers_and_special_characters(self):
        # Test cases with numbers and special characters
        self.assertFalse(is_abecedarian("a1b2c3"))
        self.assertTrue(is_abecedarian("123abc"))
        self.assertFalse(is_abecedarian("a!b@c#"))
        self.assertFalse(is_abecedarian("a1c2b3"))
        self.assertFalse(is_abecedarian("a!c@b#"))


if __name__ == '__main__':
    unittest.main()
