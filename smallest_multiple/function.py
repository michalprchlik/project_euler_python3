# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def get_list_of_numbers(max_number):
	result = []
	for x in range(1, max_number + 1):
		result.append(x)
	return result 
	
def get_smallest_number_that_can_be_divided(list_of_numbers):
	result = 0
	x = 1
	lenght = len(list_of_numbers)
	
	while result == 0:
		x = x + 1
		for number in list_of_numbers:
			if x % number != 0:
				 break
			if number == list_of_numbers[-1]:
				result = x
			
	return result
