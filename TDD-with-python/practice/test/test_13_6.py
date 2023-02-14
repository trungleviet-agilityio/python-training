"""Requirements: write a program that uses set subtraction to find words in the
book that are not in the word list."""

import unittest
import string


def book_words():
    '''
      This function reads file (book), breaks it into
      a list of used words in lower case.
    '''
    with open('../tsawyer.txt', 'r') as book:
        text = book.read().replace('\n', '')
        # Remove punctuation and split the text into words
        words_list = ''.join(c.lower()
                             for c in text if c not in string.punctuation).split()

    return words_list


def words_list():
    '''
      This function returns words list from words.txt file.
    '''
    res = []
    with open('../words.txt') as fin:
        for line in fin:
            # read each line from the file and strip whitespace to get a list of words
            word = line.strip()
            res.append(word)
    return res


def avoids():
    '''
    This function finds all the words in the book file that are not in the words file.
    '''
    set1 = set(book_words())
    set2 = set(words_list())
    res = set1 - set2
    return res


class TestBookWords(unittest.TestCase):

    def test_book_words_returns_list(self):
        # Test that book_words() returns a list
        result = book_words()
        self.assertIsInstance(result, list)

    def test_book_words_returns_non_empty_list(self):
        # Test that book_words() returns a non-empty list
        result = book_words()
        self.assertGreater(len(result), 0)

    def test_words_list_returns_list(self):
        # Test that words_list() returns a list
        result = words_list()
        self.assertIsInstance(result, list)

    def test_words_list_returns_non_empty_list(self):
        # Test that words_list() returns a non-empty list
        result = words_list()
        self.assertGreater(len(result), 0)

    def test_avoids_contains_only_words_not_in_words_list(self):
        # Test that avoids() returns a set containing only words not in the words list
        result = avoids()
        self.assertIsInstance(result, set)
        words_set = set(result)
        words_list_set = set(words_list())
        self.assertTrue(all(word not in words_list_set for word in words_set))

    def test_avoids_contains_no_words_in_words_list(self):
        # Test that avoids() returns a set containing no words in the words list
        result = avoids()
        words_set = set(result)
        words_list_set = set(words_list())
        self.assertTrue(len(words_set.intersection(words_list_set)) == 0)


if __name__ == '__main__':
    unittest.main()
