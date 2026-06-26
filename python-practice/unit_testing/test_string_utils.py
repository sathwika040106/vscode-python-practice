import unittest
from string_utils import reverse_text, is_palindrome


class TestStrings(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse_text("Python"), "nohtyP")

    def test_palindrome(self):
        self.assertTrue(is_palindrome("Madam"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("Python"))


if __name__ == "__main__":
    unittest.main()