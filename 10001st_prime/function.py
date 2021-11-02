# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def get_xxx_prime_number(max_number):
	number = 1
	count = 0
	prime_number_list = []
	while count < max_number:
		number = number + 1
		if is_prime_number(number, prime_number_list):
			prime_number_list.append(number)
			count = len(prime_number_list)

	return number 

	
def is_prime_number(number, prime_number_list):
	result = True
	for prime_number in prime_number_list:
		if number % prime_number == 0:
			result = False
			break
	return result