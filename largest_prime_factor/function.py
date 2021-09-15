# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def get_largest_prime_number_for_number(number):
	
	divider = 2
	result = 0
	while number >= divider:
		if number % divider == 0:
			number = number / divider
			result = int(divider)
		divider = divider + 1
	return result
	