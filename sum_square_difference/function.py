# The sum of the squares of the first ten natural numbers is
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def get_sum_of_squares(max_number):
	result = 0
	for x in range(1, max_number + 1):
		result = result + x * x
	return result 
	
def get_square_of_sum(max_number):
	sum = 0
	for x in range(1, max_number + 1):
		sum = sum + x
	result = sum * sum 
	return result 

def get_result(max_number):
	sum_of_squares = get_sum_of_squares(max_number)
	square_of_sum = get_square_of_sum(max_number)
	result = square_of_sum - sum_of_squares
	return result
