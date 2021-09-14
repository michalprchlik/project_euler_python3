from function import *
import unittest

############################################

class TestFunction(unittest.TestCase):

	def test_get_numbers(self):
		max_number=1
		expected_result=[]
		result=get_numbers(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))
		
		max_number=2
		expected_result=[1]
		result=get_numbers(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))
		
		max_number=10
		expected_result=[1, 2, 3, 5, 8]
		result=get_numbers(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))
		
		max_number=20
		expected_result=[1, 2, 3, 5, 8, 13]
		result=get_numbers(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))
		
		max_number=100
		expected_result=[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
		result=get_numbers(max_number)
		self.assertEqual(expected_result, result, 'max_number = ' + str(max_number))
		
	def test_get_sum_of_numbers(self):
		list_of_numbers = [1, 2, 3, 5, 8]
		expected_result=10
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, '[1, 2, 3, 5, 8]')

		list_of_numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
		expected_result=44
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, '[1, 2, 3, 5, 8, 13, 21, 34, 55, 89]')

	def test_integration(self):
		max_number=10
		expected_result=10
		list_of_numbers=get_numbers(max_number)
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, 'max_number=10')

		max_number=100
		expected_result=44
		list_of_numbers=get_numbers(max_number)
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, 'max_number=100')

		max_number=1000
		expected_result=798
		list_of_numbers=get_numbers(max_number)
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, 'max_number=1000')

		max_number=10000
		expected_result=3382
		list_of_numbers=get_numbers(max_number)
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, 'max_number=10000')

############################################

if __name__ == '__main__':
	unittest.main()
