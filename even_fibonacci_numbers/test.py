import unittest
from function import *


class TestFunction(unittest.TestCase):

	def test_get_list_of_fibonacci_numbers(self):
		max_number = 1
		expected_result = []
		result = get_list_of_fibonacci_numbers(max_number)
		self.assertEqual(expected_result, result)

		max_number = 2
		expected_result = [1]
		result = get_list_of_fibonacci_numbers(max_number)
		self.assertEqual(expected_result, result)

		max_number = 10
		expected_result = [1, 2, 3, 5, 8]
		result = get_list_of_fibonacci_numbers(max_number)
		self.assertEqual(expected_result, result)

		max_number = 20
		expected_result = [1, 2, 3, 5, 8, 13]
		result = get_list_of_fibonacci_numbers(max_number)
		self.assertEqual(expected_result, result)

		max_number = 100
		expected_result = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
		result = get_list_of_fibonacci_numbers(max_number)
		self.assertEqual(expected_result, result)

	def test_get_sum_of_even_numbers(self):
		list_of_numbers = [1, 2, 3, 5, 8]
		expected_result = 10
		result = get_sum_of_even_numbers(list_of_numbers)
		self.assertEqual(expected_result, result)

		list_of_numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
		expected_result = 44
		result = get_sum_of_even_numbers(list_of_numbers)
		self.assertEqual(expected_result, result)

	def test_integration(self):
		max_number = 10
		expected_result = 10
		list_of_numbers = get_list_of_fibonacci_numbers(max_number)
		result = get_sum_of_even_numbers(list_of_numbers)
		self.assertEqual(expected_result, result)

		max_number = 100
		expected_result = 44
		list_of_numbers = get_list_of_fibonacci_numbers(max_number)
		result = get_sum_of_even_numbers(list_of_numbers)
		self.assertEqual(expected_result, result)

		max_number = 1000
		expected_result = 798
		list_of_numbers = get_list_of_fibonacci_numbers(max_number)
		result = get_sum_of_even_numbers(list_of_numbers)
		self.assertEqual(expected_result, result)

		max_number = 10000
		expected_result = 3382
		list_of_numbers = get_list_of_fibonacci_numbers(max_number)
		result = get_sum_of_even_numbers(list_of_numbers)
		self.assertEqual(expected_result, result)


if __name__ == '__main__':
	unittest.main()
