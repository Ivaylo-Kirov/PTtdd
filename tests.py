import unittest
from functions import sum, subtract, find_matching_substrings

class TestFunctions(unittest.TestCase):
    def test_ints(self):
        self.assertEqual(sum(2, 2), 4)

    def test_doubles(self):
        self.assertEqual(sum(1.4, 2.2), 3.6)

    def test_subtract_ints(self):
        self.assertEqual(subtract(20, 3), 17)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            sum('hello', 2)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        self.assertEqual('hello world'.split(), ['hello', 'world'])

    def test_substrings(self):
        self.assertEqual(find_matching_substrings('twone', 'one'), [2])
    
    def test_substrings_2(self):
        self.assertEqual(find_matching_substrings('twoneone', 'one'), [2, 5])


if __name__ == "__main__":
    unittest.main()