# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def get_prime_numbers(max_number):
	prime_number_list = []
	for number in range (2, max_number):

		if is_prime_number(number, prime_number_list):
			prime_number_list.append(number)

	return prime_number_list


def get_summation_of_primes(prime_number_list):
	result = 0
	for prime_number in prime_number_list:
		result = result + prime_number
	return result


def get_result(max_number):
	prime_number_list = get_prime_numbers(max_number)
	result = get_summation_of_primes(prime_number_list)
	return result


def is_prime_number(number, prime_number_list):
	result = True
	for prime_number in prime_number_list:
		if number % prime_number == 0:
			result = False
			break
	return result
