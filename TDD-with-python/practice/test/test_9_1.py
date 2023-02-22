"""Requirements:
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
"""
import unittest
from unittest.mock import mock_open, patch


def print_long_words(filename):
    """
    Finds and returns words with length greater than 20 from the given file.

    Args:
    filename (str): The file name to read from.

    Returns:
    list: A list of words with length greater than 20.
    """
    with open(filename) as fin:
        # Read all lines from the file, remove leading/trailing whitespaces and store words with length greater than 20 in a list
        result = [word.strip() for line in fin for word in line.split() if len(word.strip()) > 20]
    return result


class TestLongWords(unittest.TestCase):
    # Test class for the long_words function

    def setUp(self):
        # Runs before each test method, sets up expected results
        self.expected_short = ['a', 'in', 'the', 'on']
        self.expected_long = [
            "antidisestablishmentarianism",
            "pneumonoultramicroscopicsilicovolcanoconiosis"
        ]

    def test_file_not_found(self):
        # Test case for the scenario where the file is not found
        with self.assertRaises(FileNotFoundError):
            print_long_words("missing_file.txt")

    def test_file_with_empty_content(self):
        # Test case for the scenario where the file is empty
        with patch('builtins.open', mock_open(read_data='')):
            result = print_long_words('filename')
            expected_result = []
            self.assertEqual(result, expected_result, "Expected empty list when file is empty")

    def test_file_with_short_words(self):
        # Test case for the scenario where the file only contains short words
        with patch('builtins.open', mock_open(read_data='a in the the on')):
            result = print_long_words('filename')
            expected_result = []
            self.assertEqual(result, expected_result, "Expected empty list when file only contains short words")

    def test_print_long_words(self):
        # Call print_long_words with the filename of a file that contains long words
        with patch('builtins.open', mock_open(read_data='hello world antidisestablishmentarianism goodbye world pneumonoultramicroscopicsilicovolcanoconiosis')):
            result = print_long_words('filename')
            expected_result = self.expected_long
            self.assertListEqual(result, expected_result)

    def test_file_with_short_and_long_words(self):
        # Test case for the scenario where the file contains both short and long words
        with patch('builtins.open', mock_open(read_data='antidisestablishmentarianism a pneumonoultramicroscopicsilicovolcanoconiosis on')):
            result = print_long_words('filename')
            expected_result = self.expected_long
            self.assertListEqual(result, expected_result, "Expected only long words in the file")


if __name__ == '__main__':
    unittest.main()
