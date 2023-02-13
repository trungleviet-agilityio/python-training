"""Requirements:
Write a function called has_no_e that returns True if
the given word does not have the letter e in it.
"""
import unittest


def has_no_e(word):
    """
    Check if the given word contains the letter 'e'.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word does not contain the letter 'e', False otherwise.
    """
    return 'e' not in word.lower()


class TestHasNoE(unittest.TestCase):
    def test_word_with_e(self):
        """
        Test the case where the word contains the letter 'e'.
        """
        word = "hello"
        result = has_no_e(word)
        self.assertFalse(result, f"Expected False for word '{word}'")

    def test_word_without_e(self):
        """
        Test the case where the word does not contain the letter 'e'.
        """
        word = "hi"
        result = has_no_e(word)
        self.assertTrue(result, f"Expected True for word '{word}'")

    def test_empty_word(self):
        """
        Test the case where the word is empty.
        """
        word = ""
        result = has_no_e(word)
        self.assertTrue(
            result, f"Expected True for empty word, but got {result}")

    def test_word_with_capital_e(self):
        """
        Test the case where the word contains the letter 'E' (uppercase).
        """
        word = "HEllo"
        result = has_no_e(word)
        self.assertFalse(result, f"Expected False for word '{word}'")

    def test_word_with_special_characters(self):
        """
        Test the case where the word contains special characters.
        """
        word = "h!#$%&/()="
        result = has_no_e(word)
        self.assertTrue(result, f"Expected True for word '{word}'")


if __name__ == '__main__':
    unittest.main()
