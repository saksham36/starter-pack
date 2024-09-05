# test/test_example.py

import unittest
from code.example import add, subtract

class TestExample(unittest.TestCase):

    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
