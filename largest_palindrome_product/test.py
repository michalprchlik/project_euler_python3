from function import *
import unittest

############################################

class TestFunction(unittest.TestCase):

	def test_is_number_palindrome(self):
		number=1
		expected_result=True
		result=is_number_palindrome(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))
		
		number=11
		expected_result=True
		result=is_number_palindrome(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))
		
		number=12
		expected_result=False
		result=is_number_palindrome(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))
		
		number=101
		expected_result=True
		result=is_number_palindrome(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))
		
		number=102
		expected_result=False
		result=is_number_palindrome(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))
		
		number=9009
		expected_result=True
		result=is_number_palindrome(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))
		
		number=9008
		expected_result=False
		result=is_number_palindrome(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))
		
		number=111111
		expected_result=True
		result=is_number_palindrome(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))
		
	def test_get_largest_palindrome(self):
		expected_result=906609
		result=get_largest_palindrome()
		self.assertEqual(expected_result, result)
	

############################################

if __name__ == '__main__':
	unittest.main()
