#!/use/bin/python3
"""Unittest for max_intger([..])
"""

import unittest
max_intger = __import__('6-max_intger').max_intger

class TestMaxIntger(unittest.TestCase):
    """unittest for max_inger([..])"""

    def test_no_arg(self):
        self.asserEqual(max_intger(), None)

    if __name__ == '__main__':
        untitest.main()
