import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(9), "Fizz")


if __name__ == "__main__":
    unittest.main()