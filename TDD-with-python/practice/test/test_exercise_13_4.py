from unittest.mock import mock_open, patch
import unittest
from io import StringIO

from exercise_13_4 import BookAnalyzer


class BookAnalyzerTest(unittest.TestCase):
    # Define a constant for the open function name to reduce duplication
    BUILTINS_OPEN = 'builtins.open'

    def setUp(self):
        self.book = '../tsawyer.txt'
        self.words_file = '../words.txt'
        self.book_analyzer = BookAnalyzer()

    def test_del_punctuation(self):
        # Test the del_punctuation method with example input strings
        self.assertEqual(self.book_analyzer.del_punctuation('Tom!'), 'Tom')
        self.assertEqual(self.book_analyzer.del_punctuation('Huck,'), 'Huck')
        self.assertEqual(self.book_analyzer.del_punctuation('Good.'), 'Good')
        self.assertEqual(self.book_analyzer.del_punctuation('.Have a good, day.'), 'Have a good day')

    def test_break_into_words(self):
        # Mock the book file and test that the break_into_words method returns a list of words
        with patch(BookAnalyzerTest.BUILTINS_OPEN, mock_open(read_data='The Adventures of Tom Sawyer')):
            words_list = self.book_analyzer.break_into_words()
            self.assertListEqual(
                words_list, ['the', 'adventures', 'of', 'tom', 'sawyer'])

        # Test with empty book file
        with patch(BookAnalyzerTest.BUILTINS_OPEN, mock_open(read_data='')):
            words_list = self.book_analyzer.break_into_words()
            self.assertListEqual(words_list, [])

    def test_create_dict(self):
        # Mock the book file and test that the create_dict method returns a dictionary of word frequencies
        with patch(BookAnalyzerTest.BUILTINS_OPEN, mock_open(read_data='The Adventures of Tom Sawyer')):
            dictionary = self.book_analyzer.create_dict()
            self.assertDictEqual(
                dictionary, {'the': 1, 'adventures': 1, 'of': 1, 'tom': 1, 'sawyer': 1})

    def test_words_list(self):
        # Mock the words file and test that the words_list method returns a list of words
        with patch(BookAnalyzerTest.BUILTINS_OPEN, mock_open(read_data='cat\ndog\nbird')):
            words_list = self.book_analyzer.words_list()
            self.assertListEqual(words_list, ['cat', 'dog', 'bird'])

        # Test with empty words file
        with patch(BookAnalyzerTest.BUILTINS_OPEN, mock_open(read_data='')):
            words_list = self.book_analyzer.words_list()
            self.assertListEqual(words_list, [])

    def test_avoids(self):
        # Test the avoids method with a mocked book and words file, and verify that the expected output is printed to stdout
        mock_dict = ['the', 'of', 'and', 'to', 'in']
        mock_book = ['adventures', 'tom', 'sawyer', 'mark', 'twain']
        expected_output = "adventures\ntom\nsawyer\nmark\ntwain\n\nIn total there are 5 words which are not in words.txt file\n"

        with patch(BookAnalyzerTest.BUILTINS_OPEN, mock_open(read_data='the\nof\nand\nto\nin\n')) as mock_file, \
             patch.object(BookAnalyzer, 'break_into_words', return_value=mock_book), \
             patch.object(BookAnalyzer, 'words_list', return_value=mock_dict), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:

            BookAnalyzer.avoids()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
