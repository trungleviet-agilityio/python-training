"""Requirements:
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
"""

import unittest

# Constant for the filename of the input file
FILENAME = "words.txt"

def print_long_words(filename):
    """
    Finds and returns words with length greater than 20 from the given file.

    Args:
    filename (str): The file name to read from.

    Returns:
    str: A comma-separated string of words with length greater than 20.
    """
    with open(filename) as fin:
        # Read all lines from the file, remove leading/trailing whitespaces and store words with length greater than 20 in a list
        result = [word.strip() for word in fin if len(word.strip()) > 20]
    return ', '.join(result)


class TestPrintLongWords(unittest.TestCase):
    # Test class for the print_long_words function

    def setUp(self):
        # Runs before each test method, sets up expected results
        self.expected_short = []
        self.expected_long = [
            "antidisestablishmentarianism",
            "pneumonoultramicroscopicsilicovolcanoconiosis"
        ]

    def test_file_not_found(self):
        # Test case for the scenario where the file is not found
        with self.assertRaises(FileNotFoundError):
            print_long_words("missing_file.txt")

    def test_file_with_short_words(self):
        # Test case for the scenario where the file only contains short words
        result = print_long_words(FILENAME)
        self.assertListEqual(result, self.expected_short)

    def test_print_long_words(self):
        # Call print_long_words with the filename of a file that contains long words
        result = print_long_words(FILENAME)
        expected_result = ', '.join(self.expected_long)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
