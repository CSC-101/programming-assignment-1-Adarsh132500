import data
from data import Price
from data import Rectangle
from data import Point
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_lowercase(self):
        self.assertEqual(hw1.vowel_count("hello"), 2)

    def test_vowel_count_mixed_case(self):
        self.assertEqual(hw1.vowel_count("HeLLo"), 2)

    # Part 2
    def test_short_lists_all_two_elements(self):
        self.assertEqual(hw1.short_lists([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_short_lists_mixed(self):
        self.assertEqual(hw1.short_lists([[1, 2], [3], [4, 5], [6, 7, 8]]), [[1, 2], [4, 5]])

    # Part 3
    def test_ascending_pairs_all_two_elements(self):
        self.assertEqual(hw1.ascending_pairs([[3, 1], [4, 2]]), [[1, 3], [2, 4]])

    def test_ascending_pairs_mixed(self):
        self.assertEqual(hw1.ascending_pairs([[1, 2], [3], [6, 5], [7, 8, 9]]), [[1, 2], [3], [5, 6], [7, 8, 9]])

    # Part 4
    def test_add_prices_no_carry(self):
        price1 = Price(5, 50)
        price2 = Price(3, 25)
        result = hw1.add_prices(price1, price2)
        self.assertEqual(result, Price(8, 75))

    def test_add_prices_with_carry(self):
        price1 = Price(1, 75)
        price2 = Price(2, 50)
        result = hw1.add_prices(price1, price2)
        self.assertEqual(result, Price(4, 25))


    # Part 5
    def test_rectangle_area_positive(self):
        rect = Rectangle(Point(0, 2), Point(3, 0))
        self.assertEqual(hw1.rectangle_area(rect), 6)

    def test_rectangle_area_square(self):
        rect = Rectangle(Point(0, 5), Point(5, 0))
        self.assertEqual(hw1.rectangle_area(rect), 25)


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
