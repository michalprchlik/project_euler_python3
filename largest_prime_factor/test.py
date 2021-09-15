from function import *
import unittest

############################################

class TestFunction(unittest.TestCase):
	
	def test_get_largest_prime_number_for_number(self):
		number=2
		expected_result=2
		result=get_largest_prime_number_for_number(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))

		number=14
		expected_result=7
		result=get_largest_prime_number_for_number(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))

		number=20
		expected_result=5
		result=get_largest_prime_number_for_number(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))
			
		number=13195
		expected_result=29
		result=get_largest_prime_number_for_number(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))	
			
		number=600851475143
		expected_result=6857
		result=get_largest_prime_number_for_number(number)
		self.assertEqual(expected_result, result, 'number = ' + str(number))	
			
############################################

if __name__ == '__main__':
	unittest.main()
