import unittest

# AttribLoader class


class AttribLoader(unittest.TestLoader):
    """Class to filter test case names, given an attribute name"""

    def __init__(self, attrib):
        """Set the attribute name to be used when filtering test case names"""
        self.attrib = attrib

    def loadTestsFromModule(self, module, use_load_tests=False):
        """Override default implementation of `unittest.TestLoader`"""
        return super().loadTestsFromModule(module, use_load_tests=False)

    def getTestCaseNames(self, testCaseClass):
        """Filter test case names using a provided attribute"""
        test_names = super().getTestCaseNames(testCaseClass)
        filtered_test_names = [test
                               for test in test_names
                               if hasattr(getattr(testCaseClass, test),
                                          self.attrib)]
        return filtered_test_names
