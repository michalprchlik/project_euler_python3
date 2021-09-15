from function import *
import unittest

############################################

class TestFunction(unittest.TestCase):

	def test_get_list_of_numbers(self):

		max_number=5
		expected_result=[1, 2, 3, 4, 5]
		result=get_list_of_numbers(max_number)
		self.assertEqual(expected_result, result, 'max_number = 5')
		
		max_number=10
		expected_result=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		result=get_list_of_numbers(max_number)
		self.assertEqual(expected_result, result, 'max_number = 10')
	
	def test_get_smallest_number_that_can_be_divided(self):
		list_of_numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		expected_result = 2520
		result = get_smallest_number_that_can_be_divided(list_of_numbers)
		self.assertEqual(expected_result, result)
		

############################################

if __name__ == '__main__':
	unittest.main()
