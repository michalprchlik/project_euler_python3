
import unittest

from function import *


class TestFunction(unittest.TestCase):

	def test_get_xxx_prime_number(self):
		max_number = 1
		expected_result = 2
		result = get_xxx_prime_number(max_number)
		self.assertEqual(expected_result, result)

		max_number = 3
		expected_result = 5
		result = get_xxx_prime_number(max_number)
		self.assertEqual(expected_result, result)

		max_number = 5
		expected_result = 11
		result = get_xxx_prime_number(max_number)
		self.assertEqual(expected_result, result)

		max_number = 10
		expected_result = 29
		result = get_xxx_prime_number(max_number)
		self.assertEqual(expected_result, result)

	def test_is_prime_number(self):
		number = 10
		list_of_prime_numbers = [2, 3, 5, 7]
		expected_result = False
		result = is_prime_number(number, list_of_prime_numbers)
		self.assertEqual(expected_result, result)

		number = 13
		list_of_prime_numbers = [2, 3, 5, 7]
		expected_result = True
		result = is_prime_number(number, list_of_prime_numbers)
		self.assertEqual(expected_result, result)

		number = 14
		list_of_prime_numbers = [2, 3, 5, 7]
		expected_result = False
		result = is_prime_number(number, list_of_prime_numbers)
		self.assertEqual(expected_result, result)


if __name__ == '__main__':
	unittest.main()
