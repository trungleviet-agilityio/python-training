"""Requirements: write a program that uses set subtraction to find words in the
book that are not in the word list."""

import unittest
import string

WORDS_FILE_PATH = 'words.txt'
BOOK_WORDS_FILE_PATH = 'tsawyer.txt'

def book_words(file_path):
    """
    This function reads a file at the given file path, breaks it into
    a list of lowercase words with punctuation removed.
    """
    with open(file_path, 'r') as f:
        text = f.read().replace('\n', '')
        # Remove punctuation and split the text into words
        words_list = [word.lower() for word in text.split() if word not in string.punctuation]

    return words_list


def words_list(file_path):
    """
    This function reads a file at the given file path and returns a list of its lines,
    with leading and trailing whitespace removed.
    """
    with open(file_path) as fin:
        return [line.strip() for line in fin]


def avoids():
    """
    This function finds all the words in the book file that are not in the words file.
    """
    set1 = set(book_words(BOOK_WORDS_FILE_PATH))
    set2 = set(words_list(WORDS_FILE_PATH))
    res = set1 - set2
    return res


class TestBookWords(unittest.TestCase):

    def test_book_words_returns_list(self):
        # Test that book_words() returns a list
        result = book_words(BOOK_WORDS_FILE_PATH)
        self.assertIsInstance(result, list)

    def test_book_words_returns_non_empty_list(self):
        # Test that book_words() returns a non-empty list
        result = book_words(BOOK_WORDS_FILE_PATH)
        self.assertGreater(len(result), 0)

    def test_words_list_returns_list(self):
        # Test that words_list() returns a list
        result = words_list(WORDS_FILE_PATH)
        self.assertIsInstance(result, list)

    def test_words_list_returns_non_empty_list(self):
        # Test that words_list() returns a non-empty list
        result = words_list(WORDS_FILE_PATH)
        self.assertGreater(len(result), 0)

    def test_avoids_contains_only_words_not_in_words_list(self):
        # Test that avoids() returns a set containing only words not in the words list
        result = avoids()
        self.assertIsInstance(result, set)
        words_set = set(result)
        words_list_set = set(words_list(WORDS_FILE_PATH))
        self.assertTrue(all(word not in words_list_set for word in words_set))

    def test_avoids_contains_no_words_in_words_list(self):
        # Test that avoids() returns a set containing no words in the words list
        result = avoids()
        words_set = set(result)
        words_list_set = set(words_list(WORDS_FILE_PATH))
        self.assertTrue(len(words_set.intersection(words_list_set)) == 0)


if __name__ == '__main__':
    unittest.main()
