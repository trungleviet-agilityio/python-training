"""Requirements:
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
"""

import unittest


def print_long_words(filename):
    """
    Finds and returns words with length greater than 20 from the given file.

    Args:
    filename (str): The file name to read from.

    Returns:
    list: A list of words with length greater than 20.
    """
    with open('words.txt') as fin:
        # Read all lines from the file, remove leading/trailing whitespaces and store words with length greater than 20 in a list
        result = [word.strip() for word in fin if len(word) > 20]
    return result


class TestPrintLongWords(unittest.TestCase):
    def test_print_long_words(self):
        """
        Test if the `print_long_words` function returns the correct words.
        """
        words = print_long_words("words.txt")
        # Check if the list of words is not empty
        self.assertGreater(len(words), 0)
        for word in words:
            # Check if the length of each word is greater than or equal to 20
            self.assertGreaterEqual(len(word), 20)


if __name__ == '__main__':
    unittest.main()
