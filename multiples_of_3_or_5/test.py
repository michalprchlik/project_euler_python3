from function import *
import unittest

############################################

class TestFunction(unittest.TestCase):

	def test_get_numbers(self):
		max_number=-1
		expected_result=[]
		result=get_numbers(max_number)
		self.assertEqual(expected_result, result, 'Negative max_number')
		
		max_number=0
		expected_result=[]
		result=get_numbers(max_number)
		self.assertEqual(expected_result, result, 'max_number = 0')
		
		max_number=10
		expected_result=[0, 3, 5, 6, 9]
		result=get_numbers(max_number)
		self.assertEqual(expected_result, result, 'max_number = 0')
		
		max_number=20
		expected_result=[0, 3, 5, 6, 9, 10, 12, 15, 18]
		result=get_numbers(max_number)
		self.assertEqual(expected_result, result, 'max_number = 0')

	def test_get_sum_of_numbers(self):
		list_of_numbers = []
		expected_result=0
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, '[]')

		list_of_numbers = [0, 3, 5, 6, 9]
		expected_result=23
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, '[0, 3, 5, 6, 9]')

	def test_integration(self):
		max_number=10
		expected_result=23
		list_of_numbers=get_numbers(max_number)
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, 'max_number=10')

		max_number=100
		expected_result=2318
		list_of_numbers=get_numbers(max_number)
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, 'max_number=100')

		max_number=1000
		expected_result=233168
		list_of_numbers=get_numbers(max_number)
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, 'max_number=1000')

		max_number=10000
		expected_result=23331668
		list_of_numbers=get_numbers(max_number)
		result=get_sum_of_numbers(list_of_numbers)
		self.assertEqual(expected_result, result, 'max_number=10000')

############################################

if __name__ == '__main__':
	unittest.main()
