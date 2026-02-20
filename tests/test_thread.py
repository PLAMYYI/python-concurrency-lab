import unittest
from thread_example import square, run_threads

class TestThreadExample(unittest.TestCase):

    def test_square_positive(self):
        self.assertEqual(square(4), 16)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)

    def test_square_negative(self):
        self.assertEqual(square(-3), 9)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            square("abc")

    def test_run_threads(self):
        self.assertEqual(run_threads([1, 2, 3]), [1, 4, 9])

if __name__ == "__main__":
    unittest.main()