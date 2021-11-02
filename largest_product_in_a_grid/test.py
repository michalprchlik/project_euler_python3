from function import *
import unittest

############################################


class TestFunction(unittest.TestCase):

	def test_get_result(self):
		array = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
			[13, 14, 15, 16]
		]
		max_numbers = 4

		expected_result = 43680
		result = get_result(array, max_numbers)
		self.assertEqual(expected_result, result)	

	def test_find_product_row(self):
		array = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
			[13, 14, 15, 16]
		]
		max_numbers = 4

		expected_result = 43680
		result = find_product_row(array, max_numbers)
		self.assertEqual(expected_result, result)

	def test_find_product_column(self):
		array = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
			[13, 14, 15, 16]
		]
		max_numbers = 4

		expected_result = 6144
		result = find_product_column(array, max_numbers)
		self.assertEqual(expected_result, result)

	def test_find_product_diagonal(self):
		array = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
			[13, 14, 15, 16]
		]
		max_numbers = 4

		expected_result = 1056
		result = find_product_diagonal(array, max_numbers)
		self.assertEqual(expected_result, result)

	def test_find_product_diagonal_reverse(self):
		array = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
			[13, 14, 15, 16]
		]
		max_numbers = 4

		expected_result = 3640
		result = find_product_diagonal_reverse(array, max_numbers)
		self.assertEqual(expected_result, result)	

	def test_add_number_to_array(self):
		array = [1, 2, 3, 4]
		number = 10
		max_numbers = 4
		expected_result = [2, 3, 4, 10]
		result = add_number_to_array(array, number, max_numbers)
		self.assertEqual(expected_result, result)

		array = []
		number = 10
		max_numbers = 4
		expected_result = [10]
		result = add_number_to_array(array, number, max_numbers)
		self.assertEqual(expected_result, result)

	def test_calculate_product(self):
		array = [1, 2, 3, 4]
		max_product = 0
		expected_result = 24
		result = calculate_product(array, max_product)
		self.assertEqual(expected_result, result)
		
		array = [1, 2, 3, 4]
		max_product = 100
		expected_result = 100
		result = calculate_product(array, max_product)
		self.assertEqual(expected_result, result)	

	
if __name__ == '__main__':
	unittest.main()
