import unittest
from char_count import char_count

class TestCharCount(unittest.TestCase):
    def setUp(self):
        self.char_count = char_count

    def test_main(self):
        self.assertEqual(self.char_count(""), 0)
        self.assertEqual(self.char_count("abcde"), 0)
        self.assertEqual(self.char_count("abcdeaa"), 1)
        self.assertEqual(self.char_count("abcdeaB"), 2)
        self.assertEqual(self.char_count("Indivisibilities"), 2)

if __name__ == '__main__':
    unittest.main()
