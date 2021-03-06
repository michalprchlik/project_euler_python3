from function import *
import unittest

############################################

class TestFunction(unittest.TestCase):

	def test_is_triplet_valid_invalid(self):
		i = 2
		j = 3
		k = 4
		max_number=12
		result=is_triplet_valid(i, j, k, max_number)

		expected_result=False
		self.assertEqual(expected_result, result)

	def test_is_triplet_valid_valid(self):
		i = 3
		j = 4
		k = 5
		max_number=12
		result=is_triplet_valid(i, j, k, max_number)

		expected_result=True
		self.assertEqual(expected_result, result)

	def test_find_triplet(self):
		max_number = 12
		result=find_triplet(max_number)

		expected_result = [3,4,5]
		self.assertEqual(expected_result, result)

	def test_get_product(self):
		array = [1,2,3]
		result=get_product(array)

		expected_result=6
		self.assertEqual(expected_result, result)

		array = [3,4,5]
		result=get_product(array)

		expected_result=60
		self.assertEqual(expected_result, result)
if __name__ == '__main__':
	unittest.main()
