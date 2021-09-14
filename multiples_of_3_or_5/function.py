# If we list all the natural numbers below 10 
# that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def get_numbers(max_number):
	result = []
	for x in range(max_number):
		if x % 5 == 0 or x % 3 == 0:
			result.append(x)
	return result 
	
def get_sum_of_numbers(list_of_numbers):
	result = sum(list_of_numbers)
	return result
