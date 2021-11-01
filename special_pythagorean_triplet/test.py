from function import *
import unittest

############################################

class TestFunction(unittest.TestCase):

	def test_is_triplet_valid_invalid(self):
		i = 2
		j = 2
		k = 3
		max_number=6
		result=is_triplet_valid(i, j, k, max_number)

		expected_result=False
		self.assertEqual(expected_result, result)

		i = 1
		j = 3
		k = 3
		max_number=6
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
		max_number=12
		result=find_triplet(max_number)

		expected_result=60
		self.assertEqual(expected_result, result)
			
if __name__ == '__main__':
	unittest.main()
