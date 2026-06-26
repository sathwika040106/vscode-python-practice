import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_student_pass(self):
        student = Student("Sathwika", 90)
        self.assertTrue(student.is_pass())

    def test_student_fail(self):
        student = Student("Rahul", 20)
        self.assertFalse(student.is_pass())


if __name__ == "__main__":
    unittest.main()