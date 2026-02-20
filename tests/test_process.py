import unittest
from process_pool_example import square, parallel_square

class TestProcessPool(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(5), 25)

    def test_parallel_multiple(self):
        self.assertEqual(parallel_square([1, 2, 3]), [1, 4, 9])

    def test_parallel_empty(self):
        self.assertEqual(parallel_square([]), [])

    def test_invalid_list(self):
        with self.assertRaises(TypeError):
            parallel_square("abc")

    def test_invalid_square_input(self):
        with self.assertRaises(TypeError):
            square("abc")

if __name__ == "__main__":
    unittest.main()