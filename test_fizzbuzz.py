import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(9), "Fizz")
        
    def test_buzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(10), "Buzz")
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(30), "FizzBuzz")
    def test_fizzbuzz_other(self):
        self.assertEqual(fizzbuzz.fizzbuzz(7), "7")



if __name__ == "__main__":
    unittest.main()