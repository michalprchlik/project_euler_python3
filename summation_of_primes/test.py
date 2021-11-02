
import unittest

from function import *

class TestFunction(unittest.TestCase):

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

	def test_get_prime_numbers(self):
		max_number = 10
		expected_result = [2, 3, 5, 7]
		result = get_prime_numbers(max_number)
		self.assertEqual(expected_result, result)

	def test_get_summation_of_primes(self):
		prime_number_list = [2, 3, 5, 7]
		expected_result = 17
		result = get_summation_of_primes(prime_number_list)
		self.assertEqual(expected_result, result)

	def test_get_result(self):
		max_number = 10
		expected_result = 17
		result = get_result(max_number)
		self.assertEqual(expected_result, result)


if __name__ == '__main__':
	unittest.main()
