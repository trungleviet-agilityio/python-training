"""Requirements: Write a function named uses_all that takes a word and
a string of required letters, and that returns True if
the word uses all the required letters at least once.
How many words are there that use all the vowels aeiou?
How about aeiouy?"""

import unittest


def uses_all(word, required_letters):
    """Returns True if the given word uses all the required letters at least once."""
    return set(required_letters).issubset(set(word))


class TestUsesAll(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up any class-level resources here
        cls.vowels = 'aeiou'
        cls.vowels_and_y = 'aeiouy'

    def test_required_letters_not_in_word(self):
        # Test that the function returns False when some required letters are not in the word
        cases = [("hello", "xyz"), ("world", "q"), ("python", "jkl")]
        for word, required_letters in cases:
            with self.subTest(word=word, required_letters=required_letters):
                self.assertFalse(uses_all(word, required_letters))

    def test_required_letters_in_word(self):
        # Test that the function returns True when all required letters are in the word
        cases = [("hello", "hl"), ("world", "dlr"), ("python", "pty")]
        for word, required_letters in cases:
            with self.subTest(word=word, required_letters=required_letters):
                self.assertTrue(uses_all(word, required_letters))

    def test_vowels_in_word(self):
        # Test how many words are there that use all the vowels aeiou
        cases = [("onomatopoeia", self.vowels), ("queueing", self.vowels)]
        for word, required_letters in cases:
            with self.subTest(word=word, required_letters=required_letters):
                self.assertTrue(uses_all(word, required_letters))

    def test_vowels_and_y_in_word(self):
        # Test how many words are there that use all the vowels aeiouy
        cases = [("sequoia", self.vowels_and_y), ("buyout", self.vowels_and_y)]
        for word, required_letters in cases:
            with self.subTest(word=word, required_letters=required_letters):
                self.assertTrue(uses_all(word, required_letters))

    def test_some_vowels_missing(self):
        # Test that the function returns False when some required vowels are missing from the word
        cases = [("banana", self.vowels), ("monkey", self.vowels)]
        for word, required_letters in cases:
            with self.subTest(word=word, required_letters=required_letters):
                self.assertFalse(uses_all(word, required_letters))

    def test_all_vowels_missing(self):
        # Test that the function returns False when all required vowels are missing from the word
        cases = [("xyz", self.vowels_and_y),
                 ("programming", self.vowels_and_y)]
        for word, required_letters in cases:
            with self.subTest(word=word, required_letters=required_letters):
                self.assertFalse(uses_all(word, required_letters))


if __name__ == '__main__':
    unittest.main()
