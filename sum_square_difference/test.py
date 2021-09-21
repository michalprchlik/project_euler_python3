from function import *
import unittest

############################################

class TestFunction(unittest.TestCase):

	def test_get_sum_of_squares(self):

		max_number=1
		expected_result=1
		result=get_sum_of_squares(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))

		max_number=2
		expected_result=5
		result=get_sum_of_squares(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))

		max_number=10
		expected_result=385
		result=get_sum_of_squares(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))

	def test_get_square_of_sum(self):
		
		max_number=1
		expected_result=1
		result=get_square_of_sum(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))
		
		max_number=2
		expected_result=9
		result=get_square_of_sum(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))
		
		max_number=10
		expected_result=3025
		result=get_square_of_sum(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))
		
	def test_get_result(self):
		
		max_number=10
		expected_result=2640
		result=get_result(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))
		
############################################

if __name__ == '__main__':
	unittest.main()
