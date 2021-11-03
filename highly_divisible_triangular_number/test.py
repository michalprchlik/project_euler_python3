
import unittest

from function import *


class TestFunction(unittest.TestCase):

	def test_initiate_list_of_primes(self):
		max_number = 100
		expected_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
		result = initiate_list_of_primes(max_number)
		self.assertEqual(result, expected_result)
		

	def test_get_divisors(self):
		number = 28
		list_of_prime_numbers = [2, 3, 5, 7, 13, 17, 19, 29, 31]
		expected_result = [1, 2, 4, 7, 14, 28]
		result = get_divisors_recursive(number, list_of_prime_numbers)
		self.assertEqual(result, expected_result)

		number = 100
		list_of_prime_numbers = [2, 3, 5, 7, 13, 17, 19, 29, 31]
		expected_result = [1, 2, 4, 5, 10, 20, 25, 50, 100]
		result = get_divisors_recursive(number, list_of_prime_numbers)
		self.assertEqual(result, expected_result)

	def test_get_triangle_number(self):
		max_divisors = 6
		expected_result = 28
		list_of_prime_numbers = [2, 3, 5, 7, 13, 17, 19, 29, 31]
		result = get_triangle_number(max_divisors, list_of_prime_numbers)
		self.assertEqual(result, expected_result)

		max_divisors = 4
		expected_result = 6
		list_of_prime_numbers = [2, 3, 5, 7, 13, 17, 19, 29, 31]
		result = get_triangle_number(max_divisors, list_of_prime_numbers)
		self.assertEqual(result, expected_result)

	def test_get_list_of_prime_numbers(self):

		list_of_prime_numbers = [2]
		new_number = 3
		expected_result = [2, 3]
		result = get_list_of_prime_numbers(list_of_prime_numbers, new_number)
		self.assertEqual(result, expected_result)

		list_of_prime_numbers = [2, 3]
		new_number = 4
		expected_result = [2, 3]
		result = get_list_of_prime_numbers(list_of_prime_numbers, new_number)
		self.assertEqual(result, expected_result)

		list_of_prime_numbers = [2, 3]
		new_number = 5
		expected_result = [2, 3, 5]
		result = get_list_of_prime_numbers(list_of_prime_numbers, new_number)
		self.assertEqual(result, expected_result)

		list_of_prime_numbers = [2, 3, 5]
		new_number = 6
		expected_result = [2, 3, 5]
		result = get_list_of_prime_numbers(list_of_prime_numbers, new_number)
		self.assertEqual(result, expected_result)

		list_of_prime_numbers = [2, 3, 5]
		new_number = 7
		expected_result = [2, 3, 5, 7]
		result = get_list_of_prime_numbers(list_of_prime_numbers, new_number)
		self.assertEqual(result, expected_result)

if __name__ == '__main__':
	unittest.main()
