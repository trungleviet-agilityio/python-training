"""Requirements: Write a function named uses_only that takes a word and a string
of letters, and that returns True if the word contains only
letters in the list.
"""

import unittest


def uses_only(word, letters):
    """
    Returns True if the word contains only letters in the list, and False otherwise.
    """
    word_set = set(word.lower())  # convert word to set of lowercase characters
    # convert list of allowed letters to set of lowercase characters
    letters_set = set(letters.lower())
    # return True if word set is a subset of letters set
    return word_set.issubset(letters_set)


class TestUsesOnly(unittest.TestCase):
    """A class to contain unit tests for the uses_only function"""

    def test_uses_only_valid_words(self):
        # Test that uses_only returns True when given a word containing only letters from the list
        valid_words = [
            ('hello', 'helo'),
            ('world', 'dlrow'),
            ('python', 'thonpy'),
            ('Hello', 'HELO'),
        ]
        for word, allowed_letters in valid_words:
            with self.subTest(word=word, allowed_letters=allowed_letters):
                self.assertTrue(uses_only(word, allowed_letters))

    def test_uses_only_invalid_words(self):
        # Test that uses_only returns False when given a word containing at least one letter not in the list
        invalid_words = [
            ('help', 'helo'),
            ('world', 'dlr'),
            ('Python3', 'Python'),
        ]
        for word, allowed_letters in invalid_words:
            with self.subTest(word=word, allowed_letters=allowed_letters):
                self.assertFalse(uses_only(word, allowed_letters))

    def test_uses_only_empty_word(self):
        # Test that uses_only returns True when given an empty word and a non-empty list of allowed letters
        allowed_letters = 'helo'
        self.assertTrue(uses_only('', allowed_letters))

    def test_uses_only_same_letters(self):
        # Test that uses_only returns True when given a word and a list containing the same letters
        word = 'hello'
        allowed_letters = 'helo'
        self.assertTrue(uses_only(word, allowed_letters))

    def test_uses_only_extra_letters(self):
        # Test that uses_only returns True when given a word and a list containing extra letters
        word = 'hello'
        allowed_letters = 'hellox'
        self.assertTrue(uses_only(word, allowed_letters))

    def test_uses_only_single_letter(self):
        # Test that uses_only returns True when given a word and a list containing a single letter
        word = 'hello'
        allowed_letters = 'h'
        self.assertFalse(uses_only(word, allowed_letters))


if __name__ == '__main__':
    unittest.main()
