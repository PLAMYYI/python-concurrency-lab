import unittest
import asyncio
from asyncio_example import async_square, run_async_tasks

class TestAsyncioExample(unittest.TestCase):

    def test_async_square(self):
        result = asyncio.run(async_square(3))
        self.assertEqual(result, 9)

    def test_zero(self):
        result = asyncio.run(async_square(0))
        self.assertEqual(result, 0)

    def test_negative(self):
        result = asyncio.run(async_square(-2))
        self.assertEqual(result, 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            asyncio.run(async_square("abc"))

    def test_run_async_tasks(self):
        result = asyncio.run(run_async_tasks([1, 2, 3]))
        self.assertEqual(result, [1, 4, 9])

if __name__ == "__main__":
    unittest.main()