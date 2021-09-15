# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def get_largest_palindrome():

	palindrome = 0
	for x in range(100, 1000):
		for y in range(100, 1000):
			number = x * y
			if is_number_palindrome(number):
				if palindrome < number:
					palindrome = number
		
	return palindrome
	
def is_number_palindrome(number):
	reverse_number = int(str(number)[::-1])
	if number == reverse_number:
		result = True
	else:
		result = False
		
	return result
