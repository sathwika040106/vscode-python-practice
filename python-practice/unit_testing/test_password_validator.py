import unittest
from password_validator import is_valid


class TestPassword(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(is_valid("python123"))

    def test_invalid_password(self):
        self.assertFalse(is_valid("abc"))


if __name__ == "__main__":
    unittest.main()