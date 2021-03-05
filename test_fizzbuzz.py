import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(9), "Fizz")
        
    def test_buzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(10), "Buzz")



if __name__ == "__main__":
    unittest.main()