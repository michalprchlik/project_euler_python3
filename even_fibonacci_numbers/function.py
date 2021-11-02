# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million,
# find the sum of the even-valued terms.


def get_list_of_fibonacci_numbers(max_number):
	current_number = 1
	result = []
	while current_number < max_number:

		result.append(current_number)
		result_lenght = len(result)

		if result_lenght == 1:
			current_number = current_number + result[-1]
		else:
			current_number = result[-1] + result[-2]

	return result


def get_sum_of_even_numbers(list_of_numbers):
	result = 0
	for number in list_of_numbers:
		if number % 2 == 0:
			result = result + number

	return result
