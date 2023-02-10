""" Requirements: Write a function named avoids that takes a word
and a string of forbidden letters, and that returns True if the
word doesnot use any of the forbidden letters.
"""

import unittest


def avoids(word: str, forbidden: str) -> bool:
    """
    Check if the given word contains any of the characters in the forbidden string.

    Args:
    word (str): The word to check.
    forbidden (str): A string of forbidden characters.

    Returns:
    bool: True if the word does not contain any of the forbidden characters, False otherwise.
    """
    return all(letter not in forbidden for letter in word)


class TestAvoids(unittest.TestCase):
    """
    Tests that check if a word avoids certain letters.
    """

    def test_avoids_with_forbidden_letters(self):
        """
        Checks if 'avoids' returns False if the given word
        contains one of the forbidden letters.
        """
        self.assertFalse(avoids("hello", "abce"))

    def test_avoids_without_forbidden_letters(self):
        """
        Checks if 'avoids' returns True if the given word
        does not contain any of the forbidden letters.
        """
        self.assertTrue(avoids("hello", "xyz"))

    def test_avoids_with_empty_word(self):
        """
        Checks if 'avoids' returns True with an
        empty word and forbidden letters.
        """
        self.assertTrue(avoids("", "abce"))

    def test_avoids_with_empty_forbidden_letters(self):
        """
        Checks if 'avoids' returns True with
        no forbidden letters provided.
        """
        self.assertTrue(avoids("hello", ""))

    def test_avoids_with_both_empty_word_and_forbidden_letters(self):
        """
        Checks if 'avoids' returns True when
        both the word and forbidden letters are empty.
        """
        self.assertTrue(avoids("", ""))


if __name__ == "__main__":
    unittest.main()
